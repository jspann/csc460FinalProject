import c1 from "../images/cc2018-1.jpeg";
import c2 from "../images/cc2018-2.jpg";
import c3 from "../images/cc2018-3.jpg";
import c4 from "../images/cc2018-4.jpg";
import c5 from "../images/cc2018-5.jpg";
import card from "../images/card.svg"
import "../app-copy.css";
import BackgroundSlider from "react-background-slider";

function Action() {
  return (
    <div className="page __action">
      <BackgroundSlider
        images={[c1, c2, c3, c4, c5]}
        duration={1}
        transition={3}
      />
      <body className="climate-action">
        <div className="title">Climate Change is Real</div>
        <div className="__text">
        {'\n\n'}
our physiological need like air, water, food, shelter, sleep and etc
          will be in severe danger earliest starting in 20 years. In xx years
          the earth is predicted to warm up xxdeg. This may seem like a small
          number but that will cause ...{" "}
    <body className="cards">
        <img src={card} className="card" alt="Maslow's Love and Belonging Need"></img>
        <img src={card} className="card" alt="Maslow's Love and Belonging Need"></img>
        <img src={card} className="card" alt="Maslow's Love and Belonging Need"></img>
        <img src={card} className="card" alt="Maslow's Love and Belonging Need"></img>
        <img src={card} className="card" alt="Maslow's Love and Belonging Need"></img>
      </body>


        </div>
        <div className="__act">
      Don’t forget that in the end, we are all victims & bystanders of climage change. Even if we don’t agree on who is to blame, we all still need to chip in. 
        <a className="__actbtn" href="/CrystalBall">So what does my future look like?</a>
      </div>
      </body>


    </div>
  );
}

export default Action;
