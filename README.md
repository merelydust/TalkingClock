<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [TalkingClock](#talkingclock)
  - [Installation](#installation)
    - [On MacOS](#on-macos)
    - [On Windows](#on-windows)
  - [Team Organization & Project Workflow](#team-organization--project-workflow)
  - [Technical Documentation & Reflection](#technical-documentation--reflection)
  - [User Manual for the GUI](#user-manual-for-the-gui)
  - [Licensing and FAIR Data Principles](#licensing-and-fair-data-principles)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TalkingClock
Talking Clock Project for VT

## Installation

We develop the web project on Chrome. For the best experience, please open our web project in Chrome, as we have not adapted to other browsers.

And we use the Web Speech API in Chrome. So please make sure your Chrome is up to date. You can check Browser compatibility [here](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API#browser_compatibility).

### On MacOS

1. Install Node.js.
   * By using installer on the official [Node.js download page](https://nodejs.org/en/download/)
   * By using [Homebrew](https://medium.com/@hayasnc/how-to-install-nodejs-and-npm-on-mac-using-homebrew-b33780287d8f)

2. Install [NPM](https://www.npmjs.com/).

3. Locate into `/TalkingClock/frontend`, run `npm install`, `npm start`

4. The command line will print something like this:

   ```bash
   Compiled successfully!
   
   You can now view frontend in the browser.
   
     Local:            http://localhost:3000
     On Your Network:  http://192.111.1.111:3000
   ```

5. Check our talking clock page in the Chrome by using the "Local" address. You can also open this page on your phone by using the "on Your Network" page.

### On Windows

TODO

## Team Organization & Project Workflow

Xiaoling (River) Lin, Yuxing (Patrick) Ouyang

Documentation: 

Workflow:

* River designed the interface, specified what libaries would be included
* River wrote the frontend, style and interaction using React.js.
* We both provide test cases to test our project. If anything went wrong, we fixed it.

## Technical Documentation & Reflection

Technical Resources used:

- Languages:
  - JavaScript
  - HTML
  - CSS
  - Python
- Libraries:
  - [React.js](https://react.dev/)
  - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
  - [Web Speech API in Chrome](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

Challenges & Possible Improvement:

* River: When I finished the major part of the code, I found it hard to add a theme customization into it. Since I didn't think about it during the process, and forgot to use CSS variable for defining colors. So it became extremely annoying if I had to rewrite all the colors. Finally I had to leave it. In the future, I should list every function I want and think about how to write it before I start.

## User Manual for the GUI

TODO

## Licensing and FAIR Data Principles

TODO
