import yt_dlp
import os

def yt_download(yt_url, directory_name, file_format):
    """
    使用 yt-dlp 下載 YouTube 媒體檔案，支援 MP4、MP3 和 WAV 格式。
    自動在當前目錄下建立新的目錄存放下載的檔案。

    :param yt_url: str, YouTube 的影片 URL。
    :param directory_name: str, 新建目錄名稱。
    :param file_format: str, 下載的檔案格式 ('mp4', 'mp3', 'wav')。
    """
    # 檢查是否支援的格式
    supported_formats = ['mp4', 'mp3', 'wav']
    if file_format not in supported_formats:
        raise ValueError(f"不支援的格式：{file_format}。僅支援：{', '.join(supported_formats)}")

    # 建立目錄
    output_dir = os.path.join(os.getcwd(), directory_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"目錄已建立：{output_dir}")

    # 設置下載選項
    output_path = os.path.join(output_dir, "download")
    ydl_opts = {
        'outtmpl': f"{output_path}.%(ext)s",  # 儲存檔案的格式
        'format': 'bestvideo+bestaudio/best',  # 最高畫質與音質
    }

    # 針對音訊格式的額外選項
    if file_format in ['mp3', 'wav']:
        ydl_opts.update({
            'format': 'bestaudio/best',  # 僅下載音訊
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # 提取音訊
                'preferredcodec': file_format,  # 音訊格式
                'preferredquality': '192',  # 音質 (192 kbps，對於 mp3)
            }],
        })

    # 使用 yt-dlp 執行下載
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
        print(f"下載完成！檔案已儲存於：{output_path}.{file_format}")
    except Exception as e:
        print(f"下載失敗：{e}")

"""
1. 安裝套件：
    pip install yt-dlp

2. 安裝 FFmpeg (Windows 版安裝)
    下載 FFmpeg: https://www.gyan.dev/ffmpeg/builds/
    下載 Release builds 中的壓縮檔，例如 ffmpeg-release-essentials.zip
    將下載的壓縮檔解壓縮到目標資料夾，例如 C:\ffmpeg
    配置環境變數：在系統變數中，找到 Path 新增 FFmpeg 的 bin 路徑

3. 說明
    yt_url: YouTube 的影片 URL。
    directory_name: 新建目錄名稱。
    file_format: 下載的檔案格式 ('mp4', 'mp3', 'wav')。

範例：
from utils.yt_download import yt_download
yt_download(yt_url="https://youtu.be/ApXoWvfEYVU?si=hFhuseqNlPM0qLju", directory_name="YT_video", file_format="mp4")
"""

