import React, { Component } from "react";
// import { Redirect, Link } from 'react-router-dom'
// import { Link, withRouter } from 'react-router'
import { connect } from "react-redux";

import PatHomePage from "./pat_Components/PatHomePage";
import HomePage from "./doc_Components/HomePage";

class Home extends Component {
  componentDidMount() {
    console.log("PROPS FOM general-Home-component", this.props);
  }
  render() {
    // console.log("THE USER IS A", localStorage.getItem("user_type"));
    if (this.props.auth.token !== null) {
      if (this.props.auth.token.user_type === "DOCTOR") {
        return (
          <div>
            <HomePage />
          </div>
        );
      } else if (this.props.auth.token.user_type === "PATIENT") {
        return <PatHomePage />;
      } else {
        return (
          <div>
            <h1>You aren't suppose to be here</h1>
          </div>
        );
      }
    } else {
      return (
        <div>
          <h1>You aren't Authenticated</h1>
        </div>
      );
    }
  }
}

const mapStateToProps = (state) => {
  return {
    auth: state.auth,
  };
};
const mapDispatchToProps = (dispatch) => ({
  // fetchDocData: () => dispatch(fetchDocData()),
});
export default connect(mapStateToProps, mapDispatchToProps)(Home);
