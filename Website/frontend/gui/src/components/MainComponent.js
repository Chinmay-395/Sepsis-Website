import React, { Component } from "react";
import { Switch, Route, Redirect, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import Home from "./HomeComponent";
import AuthenticationComponent from "./AuthenticationComponent";
import Graphvisulation from "./GraphComponent";
import Header from "./HeaderComponent";

class Main extends Component {
  componentDidMount() {
    console.log("componentDidMount ran inside Main ");

    if (this.props.auth.token == null) {
      console.log("You lost your props JACK");
    } else {
      console.log(">>>>", this.props);
    }
  }
  componentDidUpdate() {
    console.log("componentUdate>>>>", this.props);
    console.log("----", this.props.location);
  }

  PatWithId = ({ match }) => {
    console.log("THE MATCH", match);
    console.log(typeof match.params.pat_id);
    console.log(this.props);
    if (this.props.auth.token !== null) {
      console.log("The auth props", this.props.auth);
      if (this.props.auth.token.token === localStorage.getItem("token")) {
        if (
          this.props.auth.token.user_type_id ===
            parseInt(match.params.pat_id) &&
          this.props.auth.token.user_type === "PATIENT"
        ) {
          return <Graphvisulation patientId={match.params.pat_id} />;
        } else if (this.props.auth.token.user_type === "DOCTOR") {
          return <Graphvisulation patientId={match.params.pat_id} />;
        } else {
          return (
            <div>
              <h2>You are not allowed here</h2>
            </div>
          );
        }
      } else {
        // This is where the user must not come
        return <h2>You are authenticated but not suppose be here</h2>;
      }
    } else {
      return <h2>+++++You are not authenticated</h2>;
    }
  };

  render() {
    return (
      <div>
        <Header />
        <Switch>
          <Route path="/home" component={() => <Home />} />
          <Route path="/login" component={() => <AuthenticationComponent />} />
          <Route path="/stats/:pat_id" component={this.PatWithId} />
          <Redirect to="/home" />
        </Switch>
        {/* Footer component */}
      </div>
    );
  }
}
const mapStateToProps = (state) => {
  return {
    auth: state.auth,
  };
};
const mapDispatchToProps = (dispatch) => ({});
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Main));
