#All imports
import cv2

#All my classes, sub-classes, functions, procedures and recursion functions
class Vision:
    def __init__(self):
        cam = cv2.VideoCapture(1)

        while True:
            ret, frame = cam.read()
            cv2.imshow('Camera', frame)

            if cv2.waitKey(17) == ord('~'):
                break

        cam.release()
        cv2.destroyAllWindows()


Vision()