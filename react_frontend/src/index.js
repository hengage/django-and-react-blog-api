import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import reportWebVitals from './reportWebVitals';

import Footer from "./components/footer";
import Header from "./components/header";
import SignIn from "./components/login";
import SignUp from './components/register';

ReactDOM.render(
  <Router>
    <React.StrictMode>
      <Header />
      <Switch>
        <Route exact path="/" component={App} />
        <Route path='/register' component={SignUp} />
        <Route path='/login' component={SignIn} />
        {/* <Route path='logout' component={SignUp} /> */}
      </Switch>
      <Footer />
    </React.StrictMode>
    </Router>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
