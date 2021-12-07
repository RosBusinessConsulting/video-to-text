# Simple example of mpeg4 audio track to text conversion
Uses `ffmpeg` to cut the audio track from mp4 file, performs speech recognition via Vosk API and Vosk model and returns text as result. A utility for calculating metrics based on the reference text is included.

## Requirements
- Python 3.6+
- [ffmpeg](http://www.ffmpeg.org/)

## Stack
- [Vosk API](https://alphacephei.com/vosk/)
- [jiwer](https://github.com/jitsi/jiwer)

## Installation

This application utilizes `ffmpeg` to convert `.mp4` to `.wav`. You should have `ffmpeg` package installed in your system to make mpeg-4 video to text conversion work.

### Install requirements
```shell
pip install -r requirements.txt
```

### Download Vosk model
Download a model for your language from https://alphacephei.com/vosk/models and put in into `./model` directory. 

Example:
```shell
wget https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip
unzip vosk-model-ru-0.22.zip
mv vosk-model-ru-0.22 model
```

## Usage
```shell
python transcript_mp4.py some_video.mp4
```

# Metrics calculation
```shell
python wer.py <hypotesis_text_file> <reference_text_file>
```

### Example:

We have an ideal transcript for this video in russian (`./samples/ideal.txt`): https://vod-video.rbc.ru/archive/2021/12/02/den1118.folder/telecast_576p.mp4

We have also made a transcript with Vosk model for the same video (`./samples/test.txt`).

So, we can run the calculation:

```shell
python wer.py samples/test.txt samples/ideal.txt
```
Result:
```shell
WER (Words Error Rate): 0.14775815217391305
MER (Match Error Rate): 0.14164767176815368
WIL (Word Information Lost): 0.22181904843819444
WIP (Word Information Preserved): 0.7781809515618056
Hits: 2636
Substitutions: 270
Deletions: 38
Insertions: 127
```
[About the metrics](https://www.researchgate.net/profile/Phil-Green-4/publication/221478089_From_WER_and_RIL_to_MER_and_WIL_improved_evaluation_measures_for_connected_speech_recognition/links/00b4951f95799284d9000000/From-WER-and-RIL-to-MER-and-WIL-improved-evaluation-measures-for-connected-speech-recognition.pdf)
