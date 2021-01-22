import React, { useState,useEffect } from "react";
import { Switch, Route, Redirect, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import Home from "./HomeComponent";
import AuthenticationComponent from "./AuthenticationComponent";
import Graphvisulation from "./GraphComponent";
import Header from "./HeaderComponent";
import GraphDynamicComponent from "./GraphDynamicComponent"
import {connect_ws,messages } from "../hooks/socketConnection"
import PatientsOfDocComponent from "./doc_Components/PatientsOfDocComponent";


let subscription
function Main(props) {
  console.log("THE PROPS",props)
  console.log("THE LOCALSTORAGE", localStorage.getItem("token"))
  const [isLoggedIn,setLoggedIn] = useState(()=>{return window.localStorage.getItem('token') !== null})
  useEffect(()=>{
    console.log("THE USE-EFFCT RAN")
    setLoggedIn(()=>{
      console.log("THE SETLOGGIN RAN")
      if(localStorage.getItem("token") !== null && 
        props.auth.token.token === localStorage.getItem("token")){
        return true
      }
      else return false
      }
    )
  },[props.auth.token])

  console.log("THE PROPS I AM LOOKING FOR AFTER LOG-OUT",isLoggedIn)
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
        <Header logInProp={isLoggedIn} />
        <Switch>
          {isLoggedIn && props.auth.token!==null?
            <>
              <Route path="/home" component={Home} />

              {props.auth.token.user_type === "PATIENT"?
                <>
                  <Route path="/stats/:pat_id" component={Graphvisulation} />
                </>:
                <>
                  <Route path="/patient/:pat_id" component={PatientsOfDocComponent} />
                </>
              }
              <Route path="/monitor/:pat_id" component={GraphDynamicComponent} />
              <Redirect to="/home" />
              {connect_ws() }
              {dataNotificationSubscription()}
            </>:
            <>
              {console.log("LOGGED OUT AND IN RUNNING COMPONNET")}
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
