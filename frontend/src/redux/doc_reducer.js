import * as actionTypes from "./ActionTypes";

const initialState = {
  isLoading: false,
  errMess: null,
  doc_data: [],
};
export const Doc_reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.DOCDATA_FETCHED:
      return {
        ...state,
        isLoading: false,
        errMess: null,
        doc_data: action.payload,
      };

    case actionTypes.DOCDATA_LOADING:
      return { ...state, isLoading: true, errMess: null, doc_data: [] };

    case actionTypes.DOCDATA_FAILED:
      return {
        ...state,
        isLoading: false,
        errMess: action.payload,
        doc_data: [],
      };
    default:
      return state;
  }
};
