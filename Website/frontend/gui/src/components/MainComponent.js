import React, { useState,useEffect } from "react";
import { Switch, Route, Redirect, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import Home from "./HomeComponent";
import AuthenticationComponent from "./AuthenticationComponent";
import Graphvisulation from "./GraphComponent";
import Header from "./HeaderComponent";
import GraphDynamicComponent from "./GraphDynamicComponent"


function Main(props) {
  console.log("THE PROPS",props)
  const [isLoggedIn,setLoggedIn] = useState(false)
  
  useEffect(()=>{
    setLoggedIn(()=>{
      if(localStorage.getItem("token") !== null && 
        props.auth.token.token === localStorage.getItem("token")){
        return true
      }
      else return false
      }
    )
  },[props.auth.token])

  console.log("THE IS LOGGED IN state \n",isLoggedIn)

  
  return(
    <>
      <div>
        <Header />
        <Switch>
          {isLoggedIn?
            <>
              <Route path="/home" component={Home} />
              <Route path="/stats/:pat_id" component={Graphvisulation} />
              <Route path="/monitor/:pat_id" component={GraphDynamicComponent} />
              <Redirect to="/home" />
            </>:
            <>
              <Route path="/login" component={AuthenticationComponent} />
              <Redirect to="/login" />
            </>
          }
        </Switch>
      </div>
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

//{isLoggedIn?
//:}
//{/* If needed we can also make a table of the data of patient */}