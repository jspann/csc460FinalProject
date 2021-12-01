import cb from "../images/cb.png";
import "../app-copy.css";

function CrystalBall() {
  return (
    <div className="page">
      <div className="cards">
        <img
          src={cb}
          className="cb"
          alt="Crystal Ball"
        ></img>
      </div>
      <div className="__act crys">
        drop a photo of your home into the crystal and we’ll show you
        <a className="__crysbtn" href="/CrystalBallWorking">
          See My Future?
        </a>
      </div>
    </div>
  );
}

export default CrystalBall;
