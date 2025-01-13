import cv2 as cv
import numpy as np

class Detector:
    def __init__(self):
        # Załadowanie modelu YOLO v4
        self.netv4 = cv.dnn.readNet("./Model/yolov4.weights", "./Model/yolov4.cfg")

    def detect(self, frame):
        # wymiary klatki filmu
        (height, width) = frame.shape[:2]

        # Define the neural network input
        blob = cv.dnn.blobFromImage(frame, 1 / 255.0, (640, 640), swapRB=True, crop=False)
        self.netv4.setInput(blob)

        # Perform forward propagation
        output_layer_name = self.netv4.getUnconnectedOutLayersNames()
        output_layers = self.netv4.forward(output_layer_name)

        #class_ids = [] #klasa detekcji -> 0 = człowiek
        boxes = [] #bounding boxy
        confidences = [] #pewność detekcji
        indices = []

        # Loop over the output layers
        for output in output_layers:
            # Loop over the detections
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                #class_id = 0 -> osoba
                if class_id == 0 and confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence)) 
                    

        indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)            
        return boxes, indices