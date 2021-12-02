import React, {useState, useEffect } from 'react';
import arrow from "../images/arrowpg1.png";
import "../app-copy.css";

function Home() {
  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  },[]) //set second argument to invoke an empty list
  return (
    <div className="page __home">
      <p>The current time is {currentTime}</p>
      <header className="title-hero">
      <div className="title __outline">Hello, this is</div>
        <div className="title">augur</div>
      </header>
      <div className="nav">
      The meaning of augur is to predict the future especially from omens. Truth be told, we are no prophets and we certainly don’t know if you will win the lottery tommorrow. But, we are engineers; using science, logic and data we want to show you a future. 
      <a className="nav __next-page" href="/Information"> So do you want to see this future? <img src={arrow} className="arrow"alt="arrow"></img></a>
      </div>
    </div>
  );
}

export default Home;