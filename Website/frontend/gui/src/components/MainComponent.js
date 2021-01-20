import React, { useState,useEffect } from "react";
import { Switch, Route, Redirect, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import Home from "./HomeComponent";
import AuthenticationComponent from "./AuthenticationComponent";
import Graphvisulation from "./GraphComponent";
import Header from "./HeaderComponent";
import GraphDynamicComponent from "./GraphDynamicComponent"
import {connect_ws,messages } from "../hooks/socketConnection"

let subscription
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

  
  function dataNotificationSubscription(){
    subscription = messages.subscribe((message)=>{
      console.log("MESSAGE of data", message)
    })  
  }
  
  function discontinueSubscription(){
    if(subscription){
      subscription.unsubscribe()
    }
  }

  
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
              {connect_ws() }
              {dataNotificationSubscription()}
            </>:
            <>
              {discontinueSubscription()}
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
