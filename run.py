import os
import requests
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# 디렉토리 생성
os.makedirs('audios', exist_ok=True)
os.makedirs('scripts', exist_ok=True)

# 텍스트 파일에서 유튜브 링크 읽어오기
with open('youtube_urls.txt', 'r') as f:
    video_urls = [line.strip() for line in f]

# 오디오 및 스크립트 추출
for video_url in video_urls:
    # pytube를 이용해 오디오 추출
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_filename = audio_stream.default_filename
    audio_path = os.path.join('audios', audio_filename)
    audio_stream.download(output_path='audios', filename=audio_filename)

    # YoutubeTranscriptApi를 이용해 스크립트 추출
    video_id = video_url.split('=')[1] if len(video_url.split('=')) >= 2 else ''
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=['ko', 'en'])

    # 로컬에 스크립트 저장
    transcript_filename = os.path.splitext(audio_filename)[0] + '.txt'
    transcript_path = os.path.join('scripts', transcript_filename)
    with open(transcript_path, 'w') as f:
        for line in transcript:
            f.write(line['text'] + '\n')

    print(f'{audio_filename} 추출 완료!! ᕕ( ᐛ )ᕗ ')
