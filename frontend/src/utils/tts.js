export const tts = (text, lang = "en-US", rate = 1) => {
    let u = new SpeechSynthesisUtterance();
    u.text = text;
    u.lang = lang;
    u.rate = rate;
    speechSynthesis.speak(u);
}