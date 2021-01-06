import React, { useState } from "react";
import { Switch, Route, Redirect, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import Home from "./HomeComponent";
import AuthenticationComponent from "./AuthenticationComponent";
import Graphvisulation from "./GraphComponent";
import Header from "./HeaderComponent";
import GraphDynamicComponent from "./GraphDynamicComponent"


function Main(props) {
  // console.log("THE PROPS",props)
  const checkLogin = ()=>{
    if(localStorage.getItem("token") !== null && props.auth.token.token === localStorage.getItem("token")){
      // const get_user_type_id = localStorage.getItem('user_type_id');
      // const get_type = localStorage.getItem('user_type');
      return true
    }
    else return false
  }
  const [isLoggedIn,setLoggedIn] = useState(checkLogin())
  
      
  return(
    <>
    {isLoggedIn?
      (
        <div>
          <Header />
          <Switch>
            <Route path="/home" component={Home} />
            <Route path="/stats/:pat_id" component={Graphvisulation} />
            <Route path="/monitor/:pat_id" component={GraphDynamicComponent} />
            {/* If needed we can also make a table of the data of patient */}
            <Redirect to="/home" />
          </Switch>
        </div>
      )
      :<Route path="/login" component={AuthenticationComponent} />}
    </>
  )
}

const mapStateToProps = (state) => {
  return {
    auth: state.auth,
  };
};
const mapDispatchToProps = (dispatch) => ({});
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Main));
