// src/Clock.jsx
import React, { useState, useEffect } from 'react';
import { tts } from '../utils/tts';
import { lang } from '../assets/lang';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { Button, Modal, TimePicker, Tooltip, Cascader, InputNumber} from 'antd';
import { PlayCircleOutlined, SettingOutlined } from '@ant-design/icons';
import './Clock.css';
dayjs.extend(customParseFormat);

function Clock() {
  const [time, setTime] = useState(new Date());
  const [myTime, setMyTime] = useState("00:00:00");
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isSettingOpen, setIsSettingOpen] = useState(false);
  const [langCode, setLangCode] = useState('en-US');
  const [rate, setRate] = useState(1);

  const clickTestBtn = () => {
    showModal();
  }

  const showModal = () => {
    setIsModalOpen(true);
  };

  const showSetting = () => {
    setIsSettingOpen(true);
  }

  const handleOk = () => {
    setIsModalOpen(false);
  };

  const handleSettingOk = () => {
    setIsSettingOpen(false);
  }

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  const handleSettingCancel = () => {
    setIsSettingOpen(false);
  }

  const tick = () => {
    setTime(new Date());
  }

  const onChange = (time, timeString) => {
    // console.log(time, timeString);
    setMyTime(timeString);
  };

  const onLangChange = val => {
    setLangCode(val);
  }

  const onRateChange = val => {
    setRate(val);
  }

  const readMyTime = () => {
    readTime(myTime);
  }

  const readTime = (timeStr) => {
    // leave out the seconds: 01:02:03 => 01:02
    tts(timeStr.slice(0, 5), langCode ?? 'en-US', rate ?? 1);
  }

  useEffect(() => {
    const timerID = setInterval(
      () => tick(),
      1000
    );

    return function cleanup() {
      clearInterval(timerID);
    };
  }, []);

  return (
    <div className="clock-container">
      <h2>{time.toLocaleTimeString()}</h2>
      <div className="test">

      </div>
      <Button
        onClick={() => readTime(time.toLocaleTimeString())}
        style={{
          width: 200,
          fontWeight: 600,
          marginRight: 32,
        }}
      >Read Current Time</Button>
      <Button
        onClick={clickTestBtn}
        style={{
          width: 200,
          fontWeight: 600,
          marginRight: 28,
        }}
      >Read My Time</Button>
      <Tooltip title="setting">
        <Button shape="circle" icon={<SettingOutlined />} onClick={showSetting}/>
      </Tooltip>
      <Modal title="Choose Time" open={isModalOpen} onOk={handleOk} onCancel={handleCancel}>
        <TimePicker onChange={onChange} defaultValue={dayjs('00:00:00', 'HH:mm:ss')} size="large" allowClear={false} />
        <Button
          icon={<PlayCircleOutlined />}
          type="text" style={{marginLeft: 28}}
          onClick={readMyTime}
          >Play aloud</Button>
      </Modal>
      <Modal
        title="TTS Setting"
        open={isSettingOpen}
        footer={null}
        onOk={handleSettingOk}
        onCancel={handleSettingCancel}
      >
        <div className="setting-content">
          <div className="line">
            <div className="label">Language: </div>
            <div className="item">
              <Cascader
                options={lang}
                onChange={onLangChange}
                defaultValue={['en-US']}
                value={langCode}
                allowClear={false}
                placeholder="Select language..." />
            </div>
          </div>
          <div className="line">
            <div className="label">Play Speed: </div>
            <div className="item">
              <InputNumber
                style={{
                  width: 200,
                }}
                defaultValue="1"
                value={rate}
                min="0.5"
                max="2"
                step="0.5"
                onChange={onRateChange}
                allowClear={false}
                stringMode
              />
            </div>
          </div>
        </div>
      </Modal>
    </div>
  );
}

export default Clock;