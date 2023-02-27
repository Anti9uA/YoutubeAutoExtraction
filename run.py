import os
import requests
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# create the directories for the audio and transcript files
os.makedirs('audios', exist_ok=True)
os.makedirs('scripts', exist_ok=True)

# read YouTube video URLs from a text file
with open('youtube_urls.txt', 'r') as f:
    video_urls = [line.strip() for line in f]

# download audio and extract transcript for each video
for video_url in video_urls:
    # download audio using pytube
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_filename = audio_stream.default_filename
    audio_path = os.path.join('audios', audio_filename)
    audio_stream.download(output_path='audios', filename=audio_filename)

    # extract transcript using YouTubeTranscriptApi
    video_id = video_url.split('=')[1] if len(video_url.split('=')) >= 2 else ''
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=['ko', 'en'])

    # save transcript to local file
    transcript_filename = os.path.splitext(audio_filename)[0] + '.txt'
    transcript_path = os.path.join('scripts', transcript_filename)
    with open(transcript_path, 'w') as f:
        for line in transcript:
            f.write(line['text'] + '\n')

    print(f'Extraction of {audio_filename} complete!')
