//authAction will be the ActionCreators for auth_reducer
import * as actionTypes from "./ActionTypes";
import axios from "axios";

export const authStart = () => {
  return {
    type: actionTypes.AUTH_START,
  };
};
export const authSuccess = (token) => {
  return {
    type: actionTypes.AUTH_SUCCESS,
    payload: token,
  };
};

export const authFail = (error) => {
  return {
    type: actionTypes.AUTH_FAIL,
    payload: error,
  };
};

export const checkAuthTimeout = (expirationTime) => {
  return (dispatch) => {
    setTimeout(() => {
      dispatch(logout());
    }, expirationTime * 1000);
  };
};

export const logout = () => {
  localStorage.removeItem("email");
  localStorage.removeItem("token");
  localStorage.removeItem("user_type");
  return {
    type: actionTypes.AUTH_LOGOUT,
    payload: null,
  };
};

export const authLogin = (username, password) => (dispatch) => {
  console.log("Authentication is enabled");
  dispatch(authStart());
  axios
    .post(`http://127.0.0.1:8000/api-auth/login/`, {
      username: username, //actually an email field will go here
      password: password,
    })
    .then((response) => {
      const token = response.data.token;
      const email = response.data.email;
      const user_type = response.data.user_type;
      localStorage.setItem("email", email);
      localStorage.setItem("token", token);
      localStorage.setItem("user_type", user_type);
      localStorage.setItem("user_type_id", response.data.user_type_id);
      // console.log("THE DATA AFTER LOGGING........", response.data)
      dispatch(authSuccess(token));
      dispatch(checkAuthTimeout(3600));
    })
    .catch((error) => dispatch(authFail(error.message)));
};

export const authSignup = (username, email, password) => (dispatch) => {
  dispatch(authStart());
  axios
    .post(`http://127.0.0.1:8000/api-auth/profile/`, {
      username: username,
      email: email,
      password: password,
    })
    .then((response) => {
      const token = response.data.key;
      const expirationDate = new Date(new Date().getTime() + 3600 * 1000); // 1 hour
      localStorage.setItem("token", token);
      localStorage.setItem("expirationDate", expirationDate);
      dispatch(authSuccess(token));
      dispatch(checkAuthTimeout(3600));
    })
    .catch((error) => dispatch(authFail(error.message)));
};

export const authCheckState = () => {
  console.log("auth check state ran");
  return (dispatch) => {
    const token = localStorage.getItem("token");
    if (token === undefined) {
      console.log(">>>> dispatching logout");
      dispatch(logout());
    } else {
      const expirationDate = new Date(localStorage.getItem("expirationDate"));
      if (expirationDate <= new Date()) {
        dispatch(logout());
      } else {
        dispatch(authSuccess(token));
        dispatch(
          checkAuthTimeout(
            (expirationDate.getTime() - new Date().getTime()) / 1000
          )
        );
      }
    }
  };
};

//docAction will be the ActionCreators for docData
export const fetchDocData = () => (dispatch) => {
  const id = localStorage.getItem("user_type_id"); // Doctor-Model-id
  dispatch(doc_dataLoading());
  let getDocData = async () => {
    await axios
      .get(`http://127.0.0.1:8000/sepsisAPI/docsdoc/${id}`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        // console.log("THE data+++++++++++++++++++++", response.data)
        // let x = response.data;
        // console.log("patient_set", x.patient_set)
        dispatch(doc_data(response.data));
      })
      .catch((error) => {
        console.log("THE ERROR+++++++++++++++", error);
        dispatch(doc_dataFailed(error.message));
      });
  };
  getDocData();
};

export const doc_data = (data) => {
  return {
    type: actionTypes.DOCDATA_FETCHED,
    payload: data,
  };
};

export const doc_dataLoading = () => {
  return {
    type: actionTypes.DOCDATA_LOADING,
  };
};

export const doc_dataFailed = (errMess) => {
  return {
    type: actionTypes.DOCDATA_FAILED,
    payload: errMess,
  };
};
