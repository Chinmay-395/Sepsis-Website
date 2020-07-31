import { combineReducers } from 'redux';
import { persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

import { Auth_reducer } from './auth_reducer';

const persistConfig = {
    key: 'root',
    storage,
    whitelist: ['auth',] //'lp_data'
}

const rootReducer = combineReducers({
    auth: Auth_reducer,
    //other data
})

export default persistReducer(persistConfig, rootReducer)