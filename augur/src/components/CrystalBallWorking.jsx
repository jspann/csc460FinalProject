import cb from "../images/cbw.png";
import "../app-copy.css";

function CrystalBallWorking() {
  return (
    <div className="page __cbworking">
      <div className="cards">
        <img
          src={cb}
          className="cb"
          alt="Crystal Ball"
        ></img>
      </div>
      <div className="title working">looking into your future</div>
    </div>
  );
}

export default CrystalBallWorking;
