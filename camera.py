'''
    File for camera object.
'''

import cv2 as cv

class Camera:
    def __init__(self, device, height, width):
        # Frame properties. Used for various calculations.
        self.height = height
        self.width = width
        self.device_no = device

        # camera capture properties
        self.camera = cv.VideoCapture(device)
        self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(cv.CAP_PROP_FRAME_WIDTH, width)

        # filter flag property: used to select filter to apply to image.
        self.filter_flag = 0    # 0 is the default image.
    
    def live_capture(self):
        while(self.camera.isOpened()):
            ret, frame = self.camera.read()
            if ret == True:
                cv.imshow("Video Feed", frame)
                key = cv.waitKey(1)
                if key == ord('q'):
                    print("Pressed Q")
                    break
                elif key == ord('a'):
                    print("Pressed A")
                elif key == ord('b'):
                    print("Pressed B")
            else:
                break
    
    def release_cam(self):
        self.camera.release()

    def choose_filter(self, img):
        if self.filter_flag == 0:
            return img
        #elif self.filter_flag == 1:
        #elif self.filter_flag == 2:
        #elif self.filter_flag == 3:
        #elif self.filter_flag == 4:
        else:
            return img
# end class

# Testbed:

myCam = Camera(0, 600, 800)
myCam.live_capture()
myCam.release_cam()