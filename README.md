# Video2frame

動画からコマ送りで画像を切り出すツール

## Usage
1. 環境構築  
- python 3系
- openCV  
` pip install opencv-python`
2. ディレクトリ構成  
```
 ROOT
 ├── video2frame.py
 ├── dataset (ここに動画を入れる)
 │    ├── a.MOV
 │    ├── b.mp4
 │    ├── c.mp4
 │    └── d.avi
 └── image_dir (ここに切り出された画像が保存される)
      ├── a_000.png
      ├── a_001.png
      └──  :
```
3. 実行  
` python video2frame.py <your fps> `  
fps : frame per second (default:10)