import cv2
import numpy as np
import matplotlib.pyplot as plt


images = ['C:/Users/Laura/Zaawansowane_programowani/photo.jpg',
          'C:/Users/Laura/Zaawansowane_programowani/photo2.jpg',
          'C:/Users/Laura/Zaawansowane_programowani/photo3.jpg']

for x in range(3):
    image = plt.imread(images[x])
    objects = None
    with open('C:/Users/Laura/Zaawansowane_programowani/coco.names', 'r') as f:
        objects = [line.strip() for line in f.readlines()]
    network = cv2.dnn.readNet('C:/Users/Laura/Zaawansowane_programowani/yolov3.cfg',
                              'C:/Users/Laura/Zaawansowane_programowani/yolov3.weights')
    network.setInput(cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False))
    layerName = network.getLayerNames()
    outputLayers = [layerName[i[0] - 1] for i in network.getUnconnectedOutLayers()]
    outs = network.forward(outputLayers)

    class_ids = []
    confidences = []
    boxes = []
    Width = image.shape[1]
    Height = image.shape[0]
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.1:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)

    cnt = 0
    for i in indices:
        i = i[0]
        box = boxes[i]
        if class_ids[i] == 0:
            label = str(objects[class_id])
            cv2.rectangle(image, (round(box[0]), round(box[1])), (round(box[0]+box[2]), round(box[1]+box[3])),
                          (0, 0, 0), 2)
            cv2.putText(image, label, (round(box[0])-10, round(box[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cnt = cnt + 1
    plt.imshow(image)
    print(f"In this photo there are {cnt} people")
    plt.show()
