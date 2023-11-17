import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import ChatDev from './pages/ChatDev';
import Navbar from './components/navbar';

function App() {
  return (
    <>
      <Navbar />
      <Router>
        <Switch>
          
          <Route exact path='/' component={ChatDev} />

        </Switch>
      </Router>
    </>
  )
}

export default App;