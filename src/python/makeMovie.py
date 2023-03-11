import cv2
import glob
from datetime import datetime
import shutil
#import shutil



date = datetime.now().strftime("%Y%m%d_%H%M%S")


images = sorted(glob.glob('/home/pi/SmartPlanter/image/*.jpg')) # 撮影した画像の読み込み。

print("画像の総枚数{0}".format(len(images)))

frame_rate = 12

width = 640
height = 480
#fourcc = cv2.VideoWriter_fourcc('m','p','4','v') # 動画のコーデックをmp指定。（ちょっと違うが）動画の拡張子を決める、    
fourcc = cv2.VideoWriter_fourcc("H", "2", "6", "4")
video = cv2.VideoWriter('/home/pi/SmartPlanter/image/latest.mp4', fourcc, frame_rate, (width, height)) # 作成する動画の情報を指定（ファイル名、拡張子、FPS、動画サイズ）。

print("動画変換中...")

for i in range(len(images)):
        # 画像を読み込む
    img = cv2.imread(images[i])
        # 画像のサイズを合わせる。
    img = cv2.resize(img,(width,height))
    video.write(img) 

video.release()
shutil.copyfile("/home/pi/SmartPlanter/image/latest.mp4", "/home.pi/Desktop/gc/top/latest.mp4")
#date_time = datetime.now().strftime("%Y%m%d%H%M%S")
#path = "/home/pi/SmartPlanter/image/" + date_time + ".mp4"
#shutil.copyfile('/home/pi/SmartPlanter/image/latest.mp4', path)
print("動画変換完了")