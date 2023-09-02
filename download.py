from pytube import YouTube, Playlist
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Download YouTube videos or playlists.")
parser.add_argument(
    "--mode",
    type=str,
    choices=["pl", "video"],
    default="video",
    help="Specify the download mode. Use 'pl' for downloading a playlist, or 'video' for a single video. Default is 'video'.",
)

args = parser.parse_args()

download_loc = "Movies"
video_url = input("Enter the URL: ")

if args.mode == "pl":
    pl = Playlist(video_url)
    print(f"Downloading playlist to {download_loc}...")
    for video in pl.videos:
        video.streams.get_highest_resolution().download(output_path=download_loc)
        print(f"Downloaded {video.title}")
else:
    video_instance = YouTube(video_url)
    stream = video_instance.streams.get_highest_resolution()
    print(f"Downloading video to {download_loc}...")
    stream.download(output_path=download_loc)
    print(f"Downloaded {video_instance.title}")
