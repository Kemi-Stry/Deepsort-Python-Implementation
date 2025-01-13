import cv2 as cv

class VideoPlayer:
    video: cv.VideoCapture
    frame_count: int
    current_frame: int

    def __init__(self, path):
        self.video = cv.VideoCapture(path)
        self.frame_count = int(self.video.get(cv.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0
    
    def play(self, detector):
        while self.video.isOpened():
            #ustatwienie aktualnej klatki
            self.video.set(cv.CAP_PROP_POS_FRAMES, self.current_frame)
            ret, frame = self.video.read()
        
            #wyjście z petli
            if not ret:
                print("Koniec video")
                break

            boxes, indices = detector.detect(frame)

            # Draw bounding boxes 
            for i in indices: 

                box = boxes[i] 
                x, y, w, h = box[0], box[1], box[2], box[3] 
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
            #wyświetlenie klatki
            cv.imshow("Video", frame)

            #sterowanie do przody / do tyłu / wyjście
            key = cv.waitKey(0)
            match key:
                case 97: #A
                    self.current_frame = max(0, self.current_frame - 1) #poprzednia klatka
                case 100: #D
                    self.current_frame = min(self.frame_count - 1, self.current_frame + 1) #następna klatka
                case 27: #ESC
                    break

            print("Aktualna klatka: ", self.current_frame)

        self.video.release()
        cv.destroyAllWindows()