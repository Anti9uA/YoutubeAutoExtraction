# YoutubeAutoExtraction
유튜브 음원추출 및 스크립트를 자동으로 추출해줍니다.

> Python 환경에서 동작합니다.  

1. requirements 설치
```
pip install -r requirements.txt
```

2. youtube_urls.txt에 추출하고자 하는 유튜브 링크를 한줄씩 구분해서 넣어주세요.    

**반드시 https://www.youtube.com/watch?v=asdfasdfasdf 와 같은 형식을 지켜서 넣어주세요!!** ❗❗
```
// ** 예제 ** //
https://www.youtube.com/watch?v=asdfasdfasd
https://www.youtube.com/watch?v=qwerqwerqwer
``` 

1. 파이썬 실행
```
python run.py
```
음원파일은 audios, 스크립트는 scripts 디렉토리에 분류되어 저장됩니다.

