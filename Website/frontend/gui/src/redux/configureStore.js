//React redux imports
import thunk from "redux-thunk";
import logger from "redux-logger";
import { createStore, applyMiddleware } from "redux";
////React-Redux-Persist
import { persistStore } from "redux-persist";

import rootReducer from "./root_reducer";

export const configureStore = () => {
  const store = createStore(rootReducer, applyMiddleware(thunk, logger));
  const persistor = persistStore(store);
  return { store, persistor };
};
