# This is a demo project about how to use yolov5 with customized data to train model of object detection.


## Step 1: put the images under sweetberry/VOCdevkit/VOC2007/JPEGImages

## Step 2: put the annotation files(.xml) under sweetberry/VOCdevkit/VOC2007/Annotations

## Step 3: Change the voc_classes.txt with your customized number of classes, run "python3 voc_annotation.py"

## Step 4: Run "python3 voc_label.py" to generate label files in ".txt" format for training, the files can be found in "labels" folder

## Step 5: Create two folders -> "images" and "labels" in "train" folder, respectively drag in the images and labels(.txt) we just generated.

## Step 6: Create two folders -> "images" and "labels" in "valid" folder, respectively drag in the images and labels(.txt) we just generated.

## Step 7: In the data.yaml file, edit your number of classes and class names in "nc" and "names".

## Step 8: Run the command "python3 train.py --img 320 --epoch 100 --data data.yaml --cfg yolov5s.yaml --weights best.pt" to start training.

## Step 9: Result will be saved under folder "runs/train"
