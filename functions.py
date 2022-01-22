import cv2
import numpy as np

from typing import *


def create_boxes(outs: List[np.ndarray],
                 image: np.ndarray,
) -> Tuple[List[List[float]], List[float], List[np.int64], np.ndarray]:
    class_ids = []
    confidences = []
    boxes = []
    width = image.shape[1]
    height = image.shape[0]
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.1:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
    return boxes, confidences, class_ids, image


def detect_people(indices: np.ndarray,
                 boxes: List[List[float]],
                 class_ids: List[np.ndarray],
                 image: np.ndarray,
                 objects: List[str],
) -> Tuple[int, np.ndarray]:
    cnt = 0
    for i in indices:
        i = i[0]
        box = boxes[i]
        if class_ids[i] == 0:
            label = str(objects[0])
            cv2.rectangle(image, (round(box[0]), round(box[1])), (round(box[0] + box[2]), round(box[1] + box[3])),
                          (0, 0, 0), 2)
            cv2.putText(image, label, (round(box[0]) - 10, round(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 0), 2)
            cnt = cnt + 1
    return (cnt, image)
