import cv2
import os
from datetime import datetime

date = datetime.now().strftime("%Y%m%d_%H%M%S")
cap = cv2.VideoCapture(0) # 任意のカメラ番号に変更する。1台だけならカメラ番号は0。
cap.set(cv2.CAP_PROP_EXPOSURE,0)
#0,-1:640ms -2:320ms -3:160ms -4:80ms -5:40ms -6:20ms -7:10ms
#-8:5ms -9:2.5ms -10:1.25ms -11:650us -12:312:us -13:150us

os.system('v4l2-ctl -d /dev/video0 -c auto_exposure=0')  #0:Auto mode 1:Manual mode
os.system('v4l2-ctl -d /dev/video0 -c iso_sensitivity_auto=1')  #0: Manual  1: Auto 
#os.system('v4l2-ctl -d /dev/video0 -c iso_sensitivity=0')        #0:0 1:100000 2:200000 3:400000 4:800000  
os.system('v4l2-ctl -d /dev/video0 -c auto_exposure=1')  #0:Auto mode 1:Manual mode
#os.system('v4l2-ctl -d /dev/video0 -c auto_exposure_bias=0')  #0-24
os.system('v4l2-ctl -d /dev/video0 -c exposure_time_absolute=5') #min=1 max=10000 default=1000
#os.system('v4l2-ctl -d /dev/video0 -c exposure_metering_mode=2') #0: Average 1:Center Weighted 2:Spot 3:Matrix 

ret, frame = cap.read() # カメラからキャプチャされた画像をframeとして読み込む


date_time = datetime.now().strftime("%Y%m%d%H%M%S")
path = "/home/pi/SmartPlanter/image/" + date_time + ".jpg"
print(path)
cv2.imwrite(path, frame) # 画像をフォルダへ保存

cap.release()
