# Compressed Object Detection (COD)
Extension of pruning and quantization to the task of object detection

In this work, we extended pruning, a compression technique which discards unnecessary model connections, and weight sharing techniques for the task of object detection. With our approach we are able to compress a state-of-the-art object detection model by 30.0% without a loss in performance. We also show that our compressed model can be easily initialized with existing pre-trained weights, and thus is able to fully utilize published state-of-the-art model zoos.

Here is the [https://gedeonmuhawenayo.github.io/files/projects/compression/AMMI_FINAL_PAPER.pdf](paper)

Our implementation is built on top of Detectron2 and Pytorch Prunning labrary.
