from datetime import datetime
import os
import platform
import tempfile
from typing import Callable, List

from gtts import gTTS, gTTSError
from pydub import AudioSegment


__all__ = [
    "Speak",
    "ChineseMashupSpeaker",
    "EnglishMashupSpeaker",
    "TurkishMashupSpeaker" "new_gtts_speaker",
]


def play_file(file: str) -> None:
    os_name = platform.system()
    if os_name == "Darwin":
        os.system(f"afplay {file}")
    elif os_name == "Linux":
        os.system(f"play {file}")


def play_audio_segment(audio: AudioSegment) -> None:
    tmp_wav = tempfile.mktemp()
    audio.export(tmp_wav, format="wav")
    play_file(tmp_wav)
    os.remove(tmp_wav)


def play_gtts(tts: gTTS) -> None:
    tmp_mp3 = tempfile.mktemp()
    tts.save(tmp_mp3)
    play_file(tmp_mp3)
    os.remove(tmp_mp3)


def concat_wav_files(files) -> AudioSegment:
    output = AudioSegment.empty()
    for file in files:
        output += AudioSegment.from_file(file, "wav")
    return output


Speak = Callable[[datetime], None]


class MashupSpeaker:
    def __init__(self, sample_dir: str, lang: str):
        self.lang = lang
        self.sample_dir = sample_dir

    def __call__(self, now_time: datetime) -> None:
        raise NotImplementedError


class ChineseMashupSpeaker(MashupSpeaker):
    def __init__(self, sample_dir: str):
        self.sample_dir = sample_dir
        super().__init__(sample_dir, "zh-CN")

    def __call__(self, now_time: datetime) -> None:
        hour = int(now_time.strftime("%I"))
        samples = [
            "pips.wav",
            *ChineseMashupSpeaker.mashup_hour(hour),
            "dian.wav",
        ]
        if now_time.minute != 0:
            samples.extend([*self.mashup_minute(now_time.minute), "fen.wav"])
        files = [os.path.join(self.sample_dir, sample) for sample in samples]
        play_audio_segment(concat_wav_files(files))

    @staticmethod
    def mashup_hour(n: int) -> List[str]:
        assert 0 < n <= 12
        if 0 < n <= 10:
            parts = [n]
        elif 10 < n <= 12:
            parts = [10, n % 10]
        else:
            parts = []
        return [f"{x:02}.wav" for x in parts]

    @staticmethod
    def mashup_minute(n: int) -> List[str]:
        assert 0 <= n <= 59
        if n == 0:
            parts = [n]
        elif 0 < n <= 10:
            parts = [0, n]
        elif 10 < n < 20:
            parts = [10, n % 10]
        elif 20 <= n <= 59:
            parts = [n // 10, 10, n % 10]
        else:
            parts = []
        return [f"{x:02}.wav" for x in parts]


class TurkishMashupSpeaker(MashupSpeaker):
    def __init__(self, sample_dir: str):
        self.sample_dir = sample_dir
        super().__init__(sample_dir, "tr")

    def __call__(self, now_time: datetime) -> None:
        samples = [
            "saat.wav",
        ]
        hour = int(now_time.strftime("%I"))

        if now_time.minute not in [0, 30]:
            if hour < 11:
                samples.append(f"{now_time.strftime('%I')}.wav")
            else:
                samples.extend(["10m.wav", f"0{hour % 10}.wav"])
            if now_time.minute == 15:
                samples.append("ceyrek.wav")
            else:
                samples.extend(self.mashup_minute(now_time.minute))
            if now_time.minute != 30:
                samples.append("gece.wav")
        else:
            if hour < 11:
                samples.append(f"{now_time.strftime('%I')}m.wav")
            else:
                samples.extend(["10m.wav", f"0{hour % 10}m.wav"])
            if now_time.minute == 30:
                samples.append("bucuk.wav")
        files = [os.path.join(self.sample_dir, sample) for sample in samples]
        play_audio_segment(concat_wav_files(files))

    @staticmethod
    def mashup_minute(n: int) -> List[str]:
        assert 1 <= n <= 59
        if n <= 10:
            parts = [n]
        elif 10 < n < 60:
            parts = [(n // 10) * 10, n % 10]
        return [f"{x:02}m.wav" for x in parts]

    @staticmethod
    def mashup_hour(hour: int) -> List[str]:
        if 0 < hour <= 10:
            str_hour = "0" + str(hour) if hour < 10 else str(hour)
            parts = [f"{str_hour}.wav"]
        elif hour > 10:
            parts = ["10m.wav", f"0{hour % 10}.wav"]
        elif hour == 0:
            parts = ["10m.wav", "02.wav"]
        return parts


class EnglishMashupSpeaker(MashupSpeaker):
    def __init__(self, sample_dir: str):
        self.sample_dir = sample_dir
        super().__init__(sample_dir, "en")

    def __call__(self, now_time: datetime) -> None:
        samples = [
            "bang.wav",
            f"{now_time.minute:02}.wav",
            "past.wav",
            f"{now_time.strftime('%I')}.wav",
        ]
        files = [os.path.join(self.sample_dir, sample) for sample in samples]
        play_audio_segment(concat_wav_files(files))


def new_gtts_speaker(lang: str) -> Speak:
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
    speaker = ChineseMashupSpeaker("../audios/zh-CN")
    speaker(datetime.now())
    speaker = EnglishMashupSpeaker("../audios/en")
    speaker(datetime.now())
    speaker = TurkishMashupSpeaker("../audios/tr")
    speaker(datetime.now())
    speaker = new_gtts_speaker("ja")
    speaker(datetime.now())
