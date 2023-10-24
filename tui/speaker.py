from datetime import datetime
import os
import platform
import tempfile

from gtts import gTTS, gTTSError
from pydub import AudioSegment


__all__ = [
    "ChineseMashupSpeaker",
    "EnglishMashupSpeaker",
    "new_gtts_speaker",
]


def concat_wav_files(*files):
    output = AudioSegment.empty()
    for file in files:
        output += AudioSegment.from_file(file, "wav")
    return output


def play_file(file: str):
    os_name = platform.system()
    if os_name == "Darwin":
        os.system(f"afplay {file}")
    elif os_name == "Linux":
        os.system(f"play {file}")


def play_audio_seg(audio_seg: AudioSegment):
    tmp_wav = tempfile.mktemp()
    audio_seg.export(tmp_wav, format="wav")
    play_file(tmp_wav)
    os.remove(tmp_wav)


def play_gtts(tts: gTTS):
    tmp_mp3 = tempfile.mktemp()
    tts.save(tmp_mp3)
    play_file(tmp_mp3)
    os.remove(tmp_mp3)


class ChineseMashupSpeaker(object):
    lang = "zh"

    def __init__(self, audio_dir):
        self.audio_dir = audio_dir

    def __call__(self, now_time: datetime):
        files = map(lambda f: os.path.join(self.audio_dir, f), [
            "pips.wav",
            *ChineseMashupSpeaker.split_number(int(now_time.strftime("%I"))),
            "dian.wav",
            *ChineseMashupSpeaker.split_number(now_time.minute),
            "fen.wav",
        ])
        play_audio_seg(concat_wav_files(*files))

    @staticmethod
    def split_number(n):
        if n < 0 or n > 100:
            return []
        if 0 < n <= 10:
            return [f"{n:02}.wav"]
        elif 10 < n < 20:
            return ["10.wav", f"{n % 10:02}.wav"]
        elif 20 <= n <= 99:
            return [f"{n // 10:02}.wav", "10.wav", f"{n % 10:02}.wav"]
        else:
            return []


class EnglishMashupSpeaker(object):
    lang = "en"

    def __init__(self, audio_dir):
        self.audio_dir = audio_dir

    def __call__(self, now_time: datetime):
        files = map(lambda f: os.path.join(self.audio_dir, f), [
            "bang.wav",
            f"{now_time.minute:02}.wav",
            "past.wav",
            f"{now_time.strftime("%I")}.wav",
        ])
        play_audio_seg(concat_wav_files(*files))


def new_gtts_speaker(lang):
    def speak(now_time: datetime):
        text = now_time.strftime("%I:%M")
        try:
            tts = gTTS(text, lang=lang)
        except gTTSError:
            return
        else:
            play_gtts(tts)
    return speak


if __name__ == "__main__":
    speaker = ChineseMashupSpeaker("../audios/zh")
    speaker(datetime.now())
    speaker = EnglishMashupSpeaker("../audios/en")
    speaker(datetime.now())
    speaker = new_gtts_speaker("ja")
    speaker(datetime.now())
