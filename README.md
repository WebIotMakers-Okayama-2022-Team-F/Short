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
Raspberry PiのOS及び必要なソフト類をインストールしてください。<BR>
必要とする環境は次の通りです。<BR>

  Raspberry Pi OS Legacy 32bit(buster)
  Python3
  OpenCV
  Node-RED
  Web-I2C-API
  MariaDB
  Grafana


### Raspberry Pi Setup
Raspberry Piはlegacyの32bit版を使用します。<BR>
Raspberry Pi Imagerを使用し、以下のOSを選択して起動用MicroSDカードを作成してください。<BR>
「OSを選ぶ」⇒「Raspberry Pi OS(other)」⇒Raspberry Pi OS(Legacy)<BR><BR>
<BR>
使用しているOSはlsb_releaseコマンドで確認できます。<BR>
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 10 (buster)
Release:	10
Codename:	buster
```

続いて、各種設定を行います。
次のコマンドでraspi-configを起動してください。
```
sudo raspi-config
```

カメラを有効化します。<BR>
[3 Interface Options]->[P1 Camera]->[<はい>]<BR>
SSHを有効化します。<BR>
[3 Interface Options]->[P2 SSH]->[<はい>]<BR>
VNCを有効化します。<BR>
[3 Interface Options]->[P3 VNC]->[<はい>]<BR>
I2Cを有効化します。<BR>
[3 Interface Options]->[P5 I2C]->[<はい>]<BR>


### Web I2C API instllation
このシステムではセンサ駆動に一部のセンサ駆動にWeb I2C APIを使用しています。Node-REDから直接センサを駆動する場合は不要です。<BR>

作業フォルダを作成してnpmとWeb-I2c-APIをインストールします。<BR>
```
mkdir Workspace
cd Workspace
npm init -y
npm install node-web-gpio node-web-i2c
```

合せてセンサを動かすためのライブラリもダウンロードします。
```
cd $HOME
wget https://github.com/chirimen-oh/chirimen/archive/refs/heads/master.zip
unzip master.zip
mv chirimen-master/ chirimen/
```

### Node-RED installation
今回はNode-REDでデバイスの操作を統合します。<BR>
次のコマンドでインストールできます。<BR>
```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

再起動時にも自動的にNode-REDが起動するようにします。<BR>
```
sudo systemctl enable nodered.service
```
詳しくは公式サイトをご確認下さい。<BR>
https://nodered.jp/docs/getting-started/raspberrypi

### MariaDB installation
集めたデータはMariaDBというMySQL互換のデータベースに蓄積します。<BR>
MariaDBのインストール方法はQiitaにまとめていますのでこちらを参考にしてください。<BR>
https://qiita.com/airpocket/items/f1dd8e0d32be6075b7de<BR>

### Grafana installation
GrafanaをRPiへインストールする方法は[公式サイトで説明されています](https://grafana.com/tutorials/install-grafana-on-raspberry-pi/)のでこの通りに進めていきます。<BR>

パッケージの認証に使用されるAPTキーを追加する。<BR>

```sh
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```

GrafanaAPTリポジトリを追加する。<BR>

```sh
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

Grafanaをインストールする。<BR>

```sh
sudo apt-get update
sudo apt-get install -y grafana
```

Grafanaサーバーを有効にする。<BR>

```sh
sudo /bin/systemctl enable grafana-server
```

Grafanaサーバーを起動する。<BR>

```sh
sudo /bin/systemctl start grafana-server
```

以上でRPi上でGrafanaが動き始めました。<BR>


### OpenCV installation
```
sudo pip3 install opencv-python
sudo apt-get install libatlas-base-dev
sudo pip3 install numpy --upgrade
``` 

### MariaDBにデータベースを作成する<BR>
MariaDBに、必要なデータベースを作成します。作成する方法にはRaspberry Pi上から直接SQL言語を使用する方法と、他のWindowsPCなどからGUIツールを使って作成する方法があります。HeidiSQLというツールを使用する方法が簡単ですので以下のページに方法をまとめています。<BR>
https://qiita.com/airpocket/items/5e73444459b7ad5b0666
<BR>
作成するデータベースは次の構成にします。<BR>
データベース名<BR>

### Node-REDでセンサを制御し、データベースへ書き込む
  Node-REDのプログラムはこちらを参照してください。
  次のノードが必要ですので事前にパレットに追加してください。
  
  node-red-contrib-ads1x15_i2c
  node-red-contrib-aedes
  node-red-contrib-bh1750
  node-red-contrib-sht
  node-red-contrib-dashboard
  node-red-node-mysql
  node-red-node-pi-gpio
  node-red-pi-neopixel

### Grafanaで可視化
  Grafanaでデータを可視化する方法は次の記事にまとめています。
  https://qiita.com/airpocket/items/61209b40f0cddf8f90ed


# license
"Smart Planter Short" by WebIoTMakers Okayama 2022 Team Farmer is licensed underCC BYSA 2.0﻿

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">クリエイティブ・コモンズ 表示 - 継承 4.0 国際 ライセンス</a>の下に提供されています。


