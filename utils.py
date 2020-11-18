import numpy as np
import torch
import os
from datetime import date, time, datetime
import detectron2
import xml.etree.ElementTree as ET
from typing import List, Tuple, Union
from fvcore.common.file_io import PathManager
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.structures import BoxMode


def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True

def handle_dirs(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def model_dir(name = '/model'):
    now = datetime.now()
    today = date.today()
    tim = str(now.hour)+'-'+str(now.minute)
    dat = str(today)
    name = name + '___' +dat + '___' + tim 
    return name

class dataset():
    def __init__(self,path='./dataset/data'):
        self.path = path

    # fmt: off
    CLASS_NAMES = ('giraffe',
                    'person',
                    'zebra',
                    'elephant',
                    'impala',
                    'monkey',
                    'lion',
                    'leopard',
                    'crocodile',
                    'buffalo',
                    'hyna',
                    'bird',
                    'gorilla')

    def load_voc_instances(self, split: str, class_names=CLASS_NAMES):
        """
        Load Pascal VOC detection annotations to Detectron2 format.
        Args:
            dirname: Contain "annotations", "images", "train.txt", "valid.txt"
            split (str): one of "train", "valid"
            class_names: list or tuple of class names
        """
        dirname = self.path

        with PathManager.open(os.path.join(dirname, split + ".txt")) as f:
            fileids = np.loadtxt(f, dtype=np.str)

        # Needs to read many small annotation files. Makes sense at local
        annotation_dirname = PathManager.get_local_path(os.path.join(dirname, "annotations/"))
        dicts = []
        for fileid in fileids:
            anno_file = os.path.join(annotation_dirname, fileid + ".xml")
            jpeg_file = os.path.join(dirname, "images/", fileid + ".jpg")

            with PathManager.open(anno_file) as f:
                tree = ET.parse(f)

            r = {
                "file_name": jpeg_file,
                "image_id": fileid,
                "height": int(tree.findall("./size/height")[0].text),
                "width": int(tree.findall("./size/width")[0].text),
            }
            instances = []

            for obj in tree.findall("object"):
                cls = obj.find("name").text
                bbox = obj.find("bndbox")
                bbox = [float(bbox.find(x).text) for x in ["xmin", "ymin", "xmax", "ymax"]]
                bbox[0] -= 1.0
                bbox[1] -= 1.0
                instances.append(
                    {"category_id": class_names.index(cls), "bbox": bbox, "bbox_mode": BoxMode.XYXY_ABS}
                )
            r["annotations"] = instances
            dicts.append(r)
        return dicts
    def register_pascal_voc(self,name, split, year, class_names=CLASS_NAMES):
        dirname = self.path
        meta_data = DatasetCatalog.register(name, lambda: self.load_voc_instances(split, class_names))
        catalog = MetadataCatalog.get(name).set(
                thing_classes=list(class_names), dirname=dirname, year=year, split=split
            )
