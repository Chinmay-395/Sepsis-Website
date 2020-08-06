import * as actionTypes from "./ActionTypes";

const initialState = {
  isLoading: true,
  errMess: null,
  pat_data: [],
};
export const Pat_reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.PATDATA_FETCHED:
      return {
        ...state,
        isLoading: false,
        errMess: null,
        pat_data: action.payload,
      };

    case actionTypes.PATDATA_LOADING:
      return { ...state, isLoading: true, errMess: null, pat_data: [] };

    case actionTypes.PATDATA_FAILED:
      return {
        ...state,
        isLoading: false,
        errMess: action.payload,
        pat_data: [],
      };
    default:
      return state;
  }
};
