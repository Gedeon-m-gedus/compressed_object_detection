# Compressed Object Detection (COD)

Authors: [Gedeon Muhawenayo](https://gedeonmuhawenayo.github.io/) and [Georgia Gkioxari](https://gkioxari.github.io/)

#### Extension of pruning and quantization to the task of object detection

In this work, we extended pruning, a compression technique which discards unnecessary model connections, and weight sharing techniques for the task of object detection. With our approach we are able to compress a state-of-the-art object detection model by 30.0% without a loss in performance. We also show that our compressed model can be easily initialized with existing pre-trained weights, and thus is able to fully utilize published state-of-the-art model zoos.

Here is the [paper](https://gedeonmuhawenayo.github.io/files/projects/compression/AMMI_FINAL_PAPER.pdf) and here is the presentation slides

Our implementation is built on top of [Detectron2](https://detectron2.readthedocs.io/) and [Pytorch Prunning labrary](https://pytorch.org/tutorials/intermediate/pruning_tutorial.html).

#### Dataset
We have collected our dataset from East African parks, it contains 1309 instances. Download the data [here](https://drive.google.com/file/d/141iHvqb_rD_WwtIhespCSA9maHzQCbb2/view?usp=sharing). The following dictionary describes the categories of animals that we are aware of and their number of instances into the dataset. Keys represent the animal category while the value represent the number of instances per that category {’giraffe’: 101, ’person’: 152, ’zebra’: 131, ’elephant’: 166, ’impala’: 169, ’monkey’: 80, ’lion’: 108, ’leopard’: 63, ’crocodile’: 61, ’buffalo’: 97, ’hyena’: 70, ’bird’: 123, ’gorilla’: 88}.

#### Results
![alt text](images/AP50.png)

#### Sample predictions from the compressed model
![alt text](images/sample_pred.png)

Pruning and quantization techniques can efficiently compress object recognition models with little loss in performance. We can prune 40% of the model with loss of a few points in average precision. The reduction in memory allows for efficient storage and enables deployment of object detectors on devices of lower computational capacity.
