import rip from "../images/maslow1.svg";
import arrow from "../images/arrowpg1.png";
import "../app-copy.css";

function Information() {
  function clickMaslow(){
    console.log("CLICKED");
  }
  return (
    <div className="page __information">
      <body className="maslow">
        <button className="maslow__tier" onClick={clickMaslow}><img src={m5} alt="Maslow's Self Actualization Need"></img></button>
        <button className="maslow__tier" onClick={clickMaslow}><img src={m4} alt="Maslow's Self Esteem Need"></img></button>
        <button className="maslow__tier" onClick={clickMaslow}><img src={m3} alt="Maslow's Love and Belonging Need"></img></button>
        <button className="maslow__tier" onClick={clickMaslow}><img src={m2} alt="Maslow's Safety Need"></img></button>
        <button className="maslow__tier" onClick={clickMaslow}><img src={m1} alt="Maslow's Physiological Need"></img></button>
      </body>
      <div className="right">
        <div className="info">
          <div className="__header">your future, your needs</div>
          <div className="__text">Maslow’s hierarchy of needs state that certain needs take precedence over others.</div>
          <div className="__text">Starting from the bottom, unless we have some satisfied state of our physiological need, we won't be able to attain the next tier, safety need.</div>
          <div className="__text">--</div>
          <div className="__text">Physiological need refers to the basics: like air, food, water and shelter</div>
          <div className="__text">Safety need refers to: personal security and health</div>
          <div className="__text">Love and belonging refers to relationships like: friendship, intimacy, family, and a sense of connection</div>
          <div className="__text">Self esteem is respect, status, recognition, freedom and strength</div>
          <div className="__text">and Self actualization is the desire to become the most that one can be</div>
          <div className="__text">--</div>
          <div className="__text">click the highest tier of the needs you have achieved</div></div>

        <div className="nav">
        What if we said your most basic need, the physiological need, will be endangered in the future.
          <a className="nav __next-page" href="/Action">
            {" "}
            What do you mean?{" "}
            <img src={arrow} className="arrow" alt="arrow"></img>
          </a>
        </div>
      </div>
    </div>
  );
}

export default Information;
