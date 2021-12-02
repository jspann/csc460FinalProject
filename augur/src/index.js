import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import {
  Home,
  // About,
  Action,
  Information,
  CrystalBall,
  CrystalBallWorking
} from "./components";

ReactDOM.render(
  <Router>
    {/* <Navigation /> */}
    <Routes>
      <Route path="/" element={<Home />} />
      {/* <Route path="/about" element={<About />} /> */}
      <Route path="/action" element={<Action/>} />
      <Route path="/information" element={<Information/>} />
      <Route path="/crystalball" element={<CrystalBall/>} />
      <Route path="/crystalballworking" element={<CrystalBallWorking/>} />

    </Routes>
  </Router>,

  document.getElementById("root")
);

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
