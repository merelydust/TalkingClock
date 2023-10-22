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

Talking Clock Project for VT

## Installation

We develop the web project on Chrome. For the best experience, please open our web project in Chrome, as we have not adapted to other browsers.

And we use the Web Speech API in Chrome. So please make sure your Chrome is up to date. You can check Browser compatibility [here](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API#browser_compatibility).

### Using Python

1. Navigate to the `build` folder

   ```bash
   cd /TalkingClock/frontend/build
   ```

2.  Start the HTTP Server

   ```bash
   python -m http.server # python3
   ```

​	This will start the server on the default port, which is 8000. You should see output similar to the following:

​	`Serving HTTP on 0.0.0.0 port 8000 ...`

3. Once the server is running, open Chrome and navigate to http://localhost:8000. Enjoy the Talking Clock!

### Using Node.js

On MacOS

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

5. Check our talking clock page in the Chrome by using the "Local" url. You can also open this page on your phone by using the "on Your Network" url .

On Windows

1. [Install Node.js and NPM](https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac)
2. The following steps are the same as those in MacOS instruction.

## Team Organization & Project Workflow

Xiaoling (River) Lin, Yuxing (Patrick) Ouyang, Ömer Tarik Özyilmaz

Documentation: 

Workflow:

* River crafted the user interface, selected the necessary libraries, and developed the frontend, encompassing the web framework, styling, and interactive elements, utilizing React.js and Ant Design. And River documented the procedure for setting up and running the web page, ensuring a seamless installation process for users.
* Patrick provided test cases to test our project. If anything went wrong, we fixed it.
* Ömer

## Technical Documentation & Reflection

Technical Resources used:

- Languages:
  - JavaScript
  - HTML
  - CSS
  - Python
- Libraries:
  - [React.js](https://react.dev/)
  - [Ant Design](https://ant.design/)
  - [Web Speech API in Chrome](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

Challenges & Possible Improvement:

* Xiaoling (River): 

  Challenges: Upon completing the principal portion of the code, I encountered difficulties incorporating a theme customization feature. Regrettably, the initial planning and process did not include the utilization of CSS variables to define colors. This omission rendered the task of rewriting all the color codes particularly exasperating. Consequently, due to time constraints, I was compelled to abandon this addition.

  Possible Improvements: Moving forward, a comprehensive listing and thoughtful contemplation of desired functionalities is imperative prior to the commencement of the coding process. This proactive approach will undoubtedly facilitate a smoother development experience and the seamless integration of various features.

## User Manual for the GUI

TODO

## Licensing and FAIR Data Principles

TODO
