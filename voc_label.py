import xml.etree.ElementTree as ET
import pickle
import os
from collections import OrderedDict
from os import listdir, getcwd
from os.path import join

sets = [('2020', 'train')]
classes = ['0', '1', '2']

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    print("start convert")
    global data_root
    in_file = open('VOCdevkit/VOC2007/Annotations/%s.xml'%(image_id), encoding='utf-8')
    out_file = open('labels/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# wd = getcwd()

for year, image_set in sets:
    # if not os.path.exists(data_root + 'VOC%s/labels/'%(year)):
    #     os.makedirs(data_root + 'VOC%s/labels/'%(year))
    image_ids = open('VOCdevkit/VOC2007/ImageSets/Main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        print(image_id)
        list_file.write('VOCdevkit/VOC2007/JPEGImages/%s.jpg\n'%(image_id))
        convert_annotation(year, image_id)
    list_file.close()

'''
fire-detect：
    train.txt
    test.txt
'''
root = r'VOCdevkit/VOC2007/JPEGImages/'
f = open(r'./2020_train.txt', 'w')
names = os.listdir(root)
for name in names:
    print(name)
    f.write(os.path.join(root, name)+'\n')
f.close()
