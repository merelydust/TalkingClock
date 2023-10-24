from datetime import datetime
import sys
from typing import Callable, Dict

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Digits, Select

import speaker


class ClockApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #clock {
        width: auto;
    }
    #selector {
        dock: bottom;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("s", "speak_time", "Speak current time"),
    ]

    languages = {
        "English": "en",
        "Chinese": "zh",
    }

    def __init__(self, speakers: Dict[str, Callable[[datetime], None]]):
        super().__init__()
        self.lang = "en"
        self.speakers = speakers

    def compose(self) -> ComposeResult:
        yield Digits("", id="clock")
        yield Select(ClockApp.languages.items(), id="selector", value="en")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%I:%M:%S %p}")

    def action_speak_time(self) -> None:
        self.get_speaker()(datetime.now())

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.lang = str(event.value)

    def get_speaker(self):
        return self.speakers.get(self.lang, speaker.new_gtts_speaker(self.lang))


def main() -> None:
    speakers: Dict[str, Callable[[datetime], None]] = {}
    for arg in sys.argv[1:]:
        lang, audio_dir = arg.split("=")
        if lang == "en":
            speakers[lang] = speaker.EnglishMashupSpeaker(audio_dir)
        elif lang == "zh":
            speakers[lang] = speaker.ChineseMashupSpeaker(audio_dir)
    app = ClockApp(speakers)
    app.run()


if __name__ == "__main__":
    main()
