// Importing modules
import React, { useState, useEffect } from "react";
import Clock from './components/Clock';
import "./App.css";
import { ClockCircleOutlined, PlayCircleOutlined } from '@ant-design/icons';
import { Menu } from 'antd';

function getItem(label, key, icon, children, type) {
  return {
    key,
    icon,
    children,
    label,
    type,
  };
}

const items = [
  getItem('Announce Time', 'sub1', <PlayCircleOutlined />, [
    getItem('Audio Recording', 'g1', null, [getItem('English', 'en'), getItem('Chinese', 'ch'),], 'group'),
    getItem('TTS Generator', 'g2', null, [getItem('English', 'tts-en'), getItem('Chinese', 'tts-ch'),], 'group'),
  ]),
  getItem('Set Alarm', 'sub2', <ClockCircleOutlined />, [
    getItem('Alarm Clock', 'alarm'),
    getItem('Countdown', 'countdown'),
  ]),

];
 
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
    });
 
    // Using useEffect for single rendering
    // useEffect(() => {
    //     // Using fetch to fetch the api from 
    //     // flask server it will be redirected to proxy
    //     fetch("/data").then((res) =>
    //         res.json().then((data) => {
    //             // Setting a data from api
    //             setdata({
    //                 name: data.Name,
    //                 age: data.Age,
    //                 date: data.Date,
    //                 programming: data.programming,
    //             });
    //         })
    //     );
    // }, []);

    const onClick = (e) => {
        console.log('click ', e);
      };
 
    return (
        <div className="App">
            <Menu
                onClick={onClick}
                theme='dark'
                style={{
                    width: 256,
                    height: '100vh',
                }}
                defaultSelectedKeys={['1']}
                defaultOpenKeys={['sub1']}
                mode="inline"
                items={items}
            />
            <div className="display">
                <Clock />
                <div className="assistant"></div>
            </div>
        </div>
    );
};
 
export default App;
