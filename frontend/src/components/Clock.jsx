// src/Clock.jsx
import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { Button, Modal, TimePicker} from 'antd';
import { PlayCircleOutlined } from '@ant-design/icons';
import './Clock.css';
dayjs.extend(customParseFormat);

function Clock() {
  const [time, setTime] = useState(new Date());
  const [myTime, setMyTime] = useState("00:00:00");
  const [isModalOpen, setIsModalOpen] = useState(false);

  const clickTestBtn = () => {
    showModal();
  }

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleOk = () => {
    setIsModalOpen(false);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  useEffect(() => {
    const timerID = setInterval(
      () => tick(),
      1000
    );

    return function cleanup() {
      clearInterval(timerID);
    };
  }, []);

  const tick = () => {
    setTime(new Date());
  }

  const onChange = (time, timeString) => {
    // console.log(time, timeString);
    setMyTime(timeString);
  };

  const readMyTime = () => {
    console.log(myTime);
  }

  return (
    <div className="clock-container">
      <h2>{time.toLocaleTimeString()}</h2>
      <div className="test">

      </div>
      <Button
        onClick={clickTestBtn}
        style={{
          fontWeight: 600,
        }}
      >Read My Time</Button>
      <Modal title="Choose Time" open={isModalOpen} onOk={handleOk} onCancel={handleCancel}>
        <TimePicker onChange={onChange} defaultValue={dayjs('00:00:00', 'HH:mm:ss')} size="large" />
        <Button
          icon={<PlayCircleOutlined />}
          type="text" style={{marginLeft: 28}}
          onClick={readMyTime}
          >Play aloud</Button>
      </Modal>
    </div>
  );
}

export default Clock;