import logo from './logo.svg';
import './App.css';

const TWITTER_ICON = 'https://codechalleng.es/static/img/icon-twitter.png'
const TIPS_ENDPOINT = 'http://127.0.0.1:8000/api/'

function Tip(props) {
    return(
        <div className="tip">
            <p>{props.tip}</p>
            {props.link && <span> (<a href={props.link} target="_blank">source</a>)</span>}
            <pre>
                {props.code}
            </pre>
            {props.share_link &&
            <p>
                <a href={props.share_link} target="_blank">
                    <img src={TWITTER_ICON} alt=""/>
                </a>
            </p>}
        </div>
    )
}

const PAGE_TITLE = 'PyBites Python Tips API'

function App() {
    return (
        <div className="App">
            <h2>{PAGE_TITLE}</h2>
            <form id="searchTips">
                <input type="text" placeholder="filter tips" value="" onChange=""/>
            </form>

            <div id="tips">
                <Tip tip="123" code="dsadsada" share_link=""></Tip>
            </div>
        </div>
    );
}

export default App;
