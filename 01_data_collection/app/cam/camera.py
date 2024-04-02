import cv2
import datetime as dt
from picamera2 import Picamera2
import datetime as dt
import numpy as np
from libcamera import controls
# importing module 
import traceback 
import os
np.set_printoptions(suppress=True)

class Camera():
    def __init__(self):
        self.cam = Picamera2()
        self.img_size = (800, 800)
        self.stream_config = self.cam.create_video_configuration({'format': 'XRGB8888',"size": self.img_size})
        self.capture_config = self.cam.create_still_configuration({'format': 'XRGB8888',"size": (1600, 1600)})
        self.cam.configure(self.stream_config)
        self.cam.start()
        self.full_res = self.cam.camera_properties['PixelArraySize']
        self.scaler_size = self.cam.capture_metadata()['ScalerCrop'][2:]
        self.scaler_crop = self.cam.capture_metadata()['ScalerCrop']
        self.beta = 0
        self.alpha = 1

        print(self.alpha)






    def zoom(self, value):

        size = [int(s * value) for s in self.scaler_size]
        offset = [(r - s) // 2 for r, s in zip(self.full_res, size)]
        self.scaler_crop = offset + size
        self.cam.set_controls({"ScalerCrop": self.scaler_crop})

    def preproc(self, image):
        image = image[:self.img_size[1], :self.img_size[0]]


        new_image = cv2.convertScaleAbs(image, alpha=self.alpha, beta=self.beta)

        
        
        return new_image


    def stream(self):
        
        while True:
            #image = self.cam.capture_array('main')
            image = self.cam.capture_array("main")
            #image = self.zoom_in(image)
            print(image.shape)
            image = self.preproc(image)

            ret, image = cv2.imencode('.jpeg', image)
            frame = image.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



    def capture(self, path, score):
        
        self.cam.switch_mode(self.capture_config)
        self.cam.set_controls({"ScalerCrop": self.scaler_crop})
        self.cam.capture_metadata()
        frame = self.cam.capture_array('main')
        print(frame.shape)
        self.cam.switch_mode(self.stream_config)
        self.cam.set_controls({"ScalerCrop": self.scaler_crop})

        file = f"{str(dt.datetime.now())}_{frame.shape[0]}x{frame.shape[1]}_{score}.jpg"
        path = os.path.join(path, file)
        out = cv2.imwrite(path, frame)

        return out



