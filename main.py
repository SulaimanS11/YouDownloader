import yt_dlp

def downloader(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("Video downloaded successfully")

downloader("https://www.youtube.com/watch?v=xI4Yisgpnmk")