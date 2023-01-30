# Short
## Discripotion
Smallest Smart Planter / 最小サイズのスマートプランター

この装置は、2022年Web×IoT メイカーズチャレンジPLUSで開発したオープンソースの水耕栽培キットです。<BR>
水耕栽培に必要な水量及び液肥の施肥の制御、気温、水温、照度の記録、LEDライトによる照明の追加、カメラによる成長記録撮影を行うことが出来ます。  
種々の制御やDBへのデータ蓄積、Webツールを使ったデータ可視化を一元的に行うため、制御にはRaspberry Pi 4Bを使用していますが、必要な機能に抑えればESP32などのマイコンを使用しても良いでしょう。  
プロジェクト名「Short」は、一株だけの最小構成の育成用に作ったことを意味しています。栽培する植物や数量に応じてハードを拡張してください。  
基本的な制御にはNode-REDを採用しているため、機能拡張や改良を行う際にも容易にプログラムの修正が可能です。  

## その他資料
Web×IoT メイカーズチャレンジPLUSの公式サイトです。  
https://webiotmakers.github.io/2022/

Web×IoT メイカーズチャレンジPLUSの最終発表時の資料です。  
https://docs.google.com/presentation/d/1nIbv-dXtBHpPwt7HMpmYs73selntcH6rF92BJmyO9pU/edit?usp=sharing


# BOM
## 購入品
|部品|数|備考|
|-|-|-|
|Raspberry Pi 4B|1||
|Raspberry Pi Camera V2.1|1||
|BH1750|1|照度センサ|
|SHT30|1|温湿度センサ|
|NeoPixel x 12 Ring|1|照明|
|NeoPixel x 16 Ring|1|照明|
|NeoPixel x 24 Ring|1|照明|
|土壌水分センサ|1|改造して水位センサとして使用|
|ねじ|いろいろ、後でまとめる||
|スペーサ|いろいろ、あとでまとめる||
|USB TypeC male to female cable|1|電源延長用|
|Wi-Fi USBドングル|1|Wi-Fi APとして運用する場合|
|φ8真鍮線 300mm|1|改造水位センサ用|
|エポキシ接着材|1|100円ショップのやつでOK　解像水位センサ用|
|方軸TTモーター|2|ポンプ駆動用|
|シリコーンゴムチューブ I.D.2×O.D.3×50cm|1|ポンプ用|
|ベアリング I.D.4×O.D.7×2.5t|16|ポンプ用|
|DRV8833モータードライバボード|1|ポンプ制御用|
|2N2222トランジスタ|1|ポンプ制御用|
|ユニバーサル基盤|2|コネクタ分配用|
|PH2.0コネクタ male 2Pin|3||
|PH2.0コネクタ female 2Pin|3||
|PH2.0コネクタ male 3Pin|1||
|PH2.0コネクタ female 3Pin|1||
|PH2.0コネクタ male 4Pin|4||
|PH2.0コネクタ female 4Pin|4||
|PH2.0コネクタ male 6Pin|2||
|PH2.0コネクタ female 6Pin|2||
|AWG26 SR被覆 ソフトワイヤ|適量||
|Dupont Pin Socket|適量||
||||
||||


# 3D Printer Parts
|パーツ名|数|備考|
|-|-|-|
|base|1|ベース|
|bottom for main tank|1|メインタンクを使用する場合の底パーツ|
|frame side layout|1|フレーム|
|frame cover|1|フレームカバー|
|main tank|1|メインタンク|
|port cover|1|Raspberry PiのUSBポートカバー|
|pot|1|栽培ポット|
|pot cover|1|main tank の上にpotを載せるカバー|
|LED blacket|1|LED、カメラを取り付けるブラケット|
|top cover|1|天面カバー|
|level sensor bracket|1|水位センサーのブラケット|
|pump_pulseless_core_for_chinaa tube|1|チューブポンプのローター|
|pump_pulseless_cover|1|チューブポンプのローターカバー|
|pump_pulseless_vertical|1|縦置き型チューブポンプケース|

# Instllation
## Hardware Assy

## Software
### Raspberry Pi Setup

### Web I2c API instllation

### Node-RED installation

### Python3 installation

### OpenCV installation


# license
"Smart Planter Short" by WebIoTMakers Okayama 2022 Team Farmer is licensed underCC BYSA 2.0﻿

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">クリエイティブ・コモンズ 表示 - 継承 4.0 国際 ライセンス</a>の下に提供されています。


