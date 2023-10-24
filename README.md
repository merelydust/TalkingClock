<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [TalkingClock](#talkingclock)
  - [Installation](#installation)
    - [Using Python](#using-python)
    - [Using Node.js](#using-nodejs)
  - [Team Organization & Project Workflow](#team-organization--project-workflow)
  - [Technical Documentation & Reflection](#technical-documentation--reflection)
  - [User Manual for the GUI](#user-manual-for-the-gui)
  - [Licensing and FAIR Data Principles](#licensing-and-fair-data-principles)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TalkingClock

Our project features two UI(user interface) types and a folder for audio recordings.

1. **Web UI:** The folder [frontend](./frontend) is a version of Web UI which offers a time announcement feature that is available in **18** different languages. Additionally, users have the option to read a custom time and adjust the speaking speed, with a range of 0.5 to 2, increasing in increments of 0.5. We have intentionally designed the speed setting in this manner to optimize the performance of Google's Web Speech API, which tends to be less effective when the speed is either extremely slow or fast. Furthermore, we have determined that a step increment of less than 0.5 is often imperceptible to human listeners, thus we have settled on 0.5 as the optimal step size.
2. **Terminal UI:** The folder [tui](./tui) contains an alternative version of the terminal UI. This version allows the system to announce the time using custom audio recordings, developed based on our mashup strategy. For additional details and instructions, please refer to its [README.md](./tui/README.md).
3. **Audios:** The folder [audios](./audios) contains audio recordings in both English and Chinese. The English recordings come from the [asterisk-tim](https://github.com/paulseward/asterisk-tim) repository on GitHub, courtesy of Paul Seward-Prior. Meanwhile, the Chinese recordings were crafted by River and Patrick, based on the rules explained by the [linguistic structure of Chinese numeral expressions](./audios/zh-CN/README.md).


## Installation

We develop the web project on **Chrome** and use its Web Speech API. For the best experience, please open our web project in Chrome, as we have not adapted to other browsers.

And make sure your Chrome is up-to-date to use the TTS ability. You can check Browser compatibility [here](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API#browser_compatibility).

### Using Python

1. Navigate to the `build` folder

   ```cd TalkingClock/frontend/build```

2. Start the HTTP Server

   ```python -m http.server 8000```
   
   This will start the server on the port 8000. You should see output similar to the following:
   
   ```Serving HTTP on 0.0.0.0 port 8000 ...```

3. Once the server is running, open Chrome and navigate to http://localhost:8000. Enjoy the Talking Clock!

### Using Node.js

On MacOS

1. Install Node.js.
   * By using installer on the official [Node.js download page](https://nodejs.org/en/download/)
   * By using [Homebrew](https://medium.com/@hayasnc/how-to-install-nodejs-and-npm-on-mac-using-homebrew-b33780287d8f)

2. Install [NPM](https://www.npmjs.com/).

3. Locate into `TalkingClock/frontend`, run `npm install`, `npm start`

4. The command line will print something like this:

   ```bash
   Compiled successfully!
   
   You can now view frontend in the browser.
   
     Local:            http://localhost:3000
     On Your Network:  http://192.111.1.111:3000
   ```

5. Check our talking clock page in the Chrome by using the "Local" url. You can also open this page on your phone by using the "on Your Network" url .

On Windows

1. [Install Node.js and NPM](https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac)
2. The following steps are the same as those in MacOS instruction.

## Team Organization & Project Workflow

Xiaoling (River) Lin, Yuxing (Patrick) Ouyang, Ömer Tarik Özyilmaz

* We use the workflow similar to [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development).

* River developed Web UI in [frontend](./frontend) folder. She crafted the user interface, including styling and interactive elements, utilizing React.js and Ant Design. And River documented the procedure for setting up and running the web page, ensuring a seamless installation process for users.
* Patrick developed TUI in [tui](./tui) folder, enabling the clock to integrate with custom audio recordings.
* Ömer contributed Turkish language support, wrote the user manual, recorded the video presentation, established the FAIR principles for the project. 
* All team members provided test cases to test our project. If anything went wrong, we fixed it.

## Technical Documentation & Reflection

Technical Resources used:

- Languages:
  - JavaScript
  - HTML
  - CSS
  - Python(3.11+)
- Libraries:
  - [React.js](https://react.dev/)
  - [Ant Design](https://ant.design/)
  - [Web Speech API in Chrome](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
  - [textual](https://github.com/Textualize/textual)
  - [gTTS](https://github.com/pndurette/gTTS)
  - [pydub](https://github.com/jiaaro/pydub)

Challenges & Possible Improvement:

* Xiaoling (River): 

  Challenges: Upon completing the principal portion of the code, I encountered difficulties incorporating a theme customization feature. Regrettably, the initial planning and process did not include the utilization of CSS variables to define colors. This omission rendered the task of rewriting all the color codes particularly exasperating. Consequently, due to time constraints, I was compelled to abandon this addition.

  Possible Improvements: Moving forward, a comprehensive listing and thoughtful contemplation of desired functionalities is imperative prior to the commencement of the coding process. This proactive approach will undoubtedly facilitate a smoother development experience and the seamless integration of various features.

* Yuxing (Patrick): The TUI version of our talking clock has certain constraints compared to its WebUI counterpart. It currently lacks features like TTS speed adjustment and time modification. Furthermore, it also lacks the potential of integrating more functionalities and AI features. The TUI approach, while appealing to tech enthusiasts, is inherently more basic and rigid. Nonetheless, it offers us a chance to interact with a talking clock directly from the terminal.

## User Manual for the GUI

TODO

## Licensing and FAIR Data Principles

TODO
