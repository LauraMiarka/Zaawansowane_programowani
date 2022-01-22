from functions import create_boxes
from functions import detect_people
import os
import matplotlib.pyplot as plt
import cv2

def main():
    path = 'C:/Users/Laura/Zaawansowane_programowani/images/'
    dir = os.listdir(path)
    for file in dir:
        image = plt.imread(path + file)
        objects = None
        with open('C:/Users/Laura/Zaawansowane_programowani/coco.names', 'r') as f:
            objects = [line.strip() for line in f.readlines()]
        network = cv2.dnn.readNet('C:/Users/Laura/Zaawansowane_programowani/yolov3.cfg',
                                  'C:/Users/Laura/Zaawansowane_programowani/yolov3.weights')
        network.setInput(cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False))
        layer_name = network.getLayerNames()
        output_layers = [layer_name[i[0] - 1] for i in network.getUnconnectedOutLayers()]
        outs = network.forward(output_layers)
        #TODO: value should be passed by reference not copy, inefficient with big images
        boxes, confidences, class_ids, image = create_boxes(outs, image)
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)
        #TODO: value should be passed by reference not copy, inefficient with big images
        cnt, image = detect_people(indices, boxes, class_ids, image, objects)

        plt.imshow(image)
        print(f"In this photo there are {cnt} people")
        plt.show()

if __name__ == '__main__':
    main()