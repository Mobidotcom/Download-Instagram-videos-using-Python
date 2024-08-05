import yt_dlp

def download_instagram_video(url):
    ydl_opts = {
        'format': 'best',  # Download the best quality video
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the name
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        print(f"Title: {info_dict['title']}")
        print(f"Uploader: {info_dict['uploader']}")
        print(f"Uploader URL: {info_dict['uploader_url']}")
        print("Download complete.")

try:
    url = input("Enter the Instagram URL: ")
    download_instagram_video(url)
except Exception as e:
    print("An error occurred:", str(e))
