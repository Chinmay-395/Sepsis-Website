import { combineReducers } from "redux";
import { persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage";

import { Auth_reducer } from "./auth_reducer";
import { Doc_reducer } from "./doc_reducer";
import { Pat_reducer } from "./pat_reducer";

const persistConfig = {
  key: "root",
  storage,
  whitelist: ["auth"], //'lp_data'
};

const rootReducer = combineReducers({
  auth: Auth_reducer,
  //other data
  doc_data: Doc_reducer,
  pat_data: Pat_reducer,
});

export default persistReducer(persistConfig, rootReducer);
