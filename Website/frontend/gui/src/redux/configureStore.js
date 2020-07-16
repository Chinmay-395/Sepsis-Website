//React redux imports
import thunk from 'redux-thunk';
import logger from 'redux-logger'
import { createStore, combineReducers, applyMiddleware } from 'redux';
//custom imports
import { Auth_reducer } from './auth_reducer'

export const configureStore = () => {
    const store = createStore(
        combineReducers({
            auth: Auth_reducer,
        }), applyMiddleware(thunk, logger)
    );
    return store;
}