//React & Redux imports
import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react'
//Custom imports
import './App.css';
import Main from './components/MainComponent';
import { configureStore } from './redux/configureStore'


const store = configureStore().store;
const persistor = configureStore().persistor

class App extends Component {

  render() {
    return (
      <Provider store={store}>
        <BrowserRouter>
          <PersistGate persistor={persistor}>
            <div className="App">
              <Main />
            </div>
          </PersistGate>
        </BrowserRouter>
      </Provider>
    );
  }
}
export default App;
