import s1 from "../images/cc2018-21.jpg";
import "../app-copy.css";

function Results() {
  function clickMaslow() {
    console.log("CLICKED");
  }
  return (
    <div className="page __information">
      <div className="maslow">
        <img className="result-img" src={s1} alt="placeholder"></img>
      </div>
      <div className="right">
        <div className="info">
          <div className="__header">we regret to inform you</div>
          <div className="__text">This is what your future looks like.</div>
          <div className="__text">
            It's wet/hot/whatever, and while it's not totally un-livable yet,
            you'll always be scared that this event might happen again...
          </div>
          <div className="__text">
            What if you have kids or grandkids? What will they go through?
          </div>
          <div className="__text">
            Well they may not be so lucky, they’ll probably have to live in this
            condition everyday.
          </div>
          <div className="__text">--</div>

          <div className="nav">
            Has this impacted your view of climate change? Is it coming sooner
            than you think? Do you feel the need to take climate change more
            seriously?
            <a className="nav __next-page" href="/Action">
              {" "}
              Send us a heart or tell us what you feel!{" "}
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Results;
