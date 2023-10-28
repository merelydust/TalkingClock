import argparse
from datetime import datetime, timedelta
from typing import Dict, Tuple

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Digits, Footer, Header, Select

import speaker


class SpeakingClock(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #clock {
        width: auto;
    }
    #selector {
        dock: bottom;
        height: 4.4;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("s", "speak_time", "Speak current time"),
    ]

    languages = {
        "English": "en",
        "Chinese": "zh-CN",
        "Turkish": "tr",
    }

    def __init__(self, lag: timedelta, speakers: Dict[str, speaker.Speak]):
        super().__init__()
        self.language = "en"
        self.lag = lag
        self.speakers = speakers

    def compose(self) -> ComposeResult:
        yield Header()
        yield Digits("", id="clock")
        yield Select(SpeakingClock.languages.items(), id="selector", value="en")
        yield Footer()

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now() + self.lag
        self.query_one(Digits).update(f"{clock:%I:%M:%S %p}")

    def action_speak_time(self) -> None:
        speak = self.speakers.get(
            self.language, speaker.new_gtts_speaker(self.language)
        )
        try:
            speak(datetime.now() + self.lag)
        except Exception as err:
            self.notify(str(err), title="Error", severity="error")

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.language = str(event.value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=str, help="specify the time")
    parsed_args, unparsed_args = parser.parse_known_args()
    lag = timedelta()
    if (time_val := parsed_args.t) is not None:
        now = datetime.now()
        time = datetime.combine(now, datetime.strptime(time_val, "%H:%M").time())
        lag = time - now
    speakers = {}
    for arg in unparsed_args:
        language, sample_dir = arg.split("=")
        match language:
            case "en":
                speakers["en"] = speaker.EnglishMashupSpeaker(sample_dir)
            case "zh" | "zh-CN":
                speakers["zh-CN"] = speaker.ChineseMashupSpeaker(sample_dir)
            case "tr":
                speakers["tr"] = speaker.TurkishMashupSpeaker(sample_dir)
            case _:
                continue

    app = SpeakingClock(lag, speakers)
    app.run()


if __name__ == "__main__":
    main()
