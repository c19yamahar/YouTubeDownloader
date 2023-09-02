# YouTube Downloader

## Description

YouTube 動画をダウンロードするプログラムです。[PyTube](https://python-pytube.readthedocs.io/en/latest/)を使用しています。  
This is a simple YouTube downloader that allows you to download videos from YouTube in different formats and qualities.  
It is written in Python and uses the [PyTube](https://python-pytube.readthedocs.io/en/latest/) library.

## Installation

次のコマンドを実行して、必要なライブラリをインストールしてください。  
Install the required libraries using pip:

```
pip install -r requirements.txt
```

その後、保存用フォルダを作ります。  
Then, create a folder to store the downloaded videos.

```
mkdir Movies
```

## Usage

次のコマンドでプログラムを実行します。  
Run the script:

```
python3 downlodad.py --mode video # for downloading a single video
python3 downlodad.py --mode pl # for downloading a playlist
```

実行後、URL を入力してください。デフォルトでは動画のダウンロードになります。  
Enter the URL of the video you want to download and press Enter.
Default mode is video, so you can just run the script without specifying the mode.

## Warning

動画のダウンロードに関しては自己責任でお願いします。  
Please use this script at your own risk.
