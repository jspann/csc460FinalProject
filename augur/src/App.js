import logo from './logo.svg';
import augurlogo from './images/augurlogo.png';
import arrow from './images/arrowpg1.png'
import './app-copy.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <img src={augurlogo} className="augurlogo" alt="logo"/>
        <h1>Hello</h1>
        <h2>we are <emph>augur</emph></h2>
        <a className="arrow-nav"
          href="/"
          target="_blank"
          rel="noopener noreferrer">and we are here to show your future</a>
        <img src={arrow} alt="arrow"></img>
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>


    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     {/* <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a> */}
    //   </header>
    // </div>
  );
}

export default App;
