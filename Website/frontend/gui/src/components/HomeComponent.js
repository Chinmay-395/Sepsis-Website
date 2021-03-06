import React from "react";
// import { Redirect, Link } from 'react-router-dom'
// import { Link, withRouter } from 'react-router'
import { Jumbotron, Button } from "reactstrap";
import { Link } from "react-router-dom";
import { connect } from "react-redux";

import PatHomePage from "./pat_Components/PatHomePage";
import HomePage from "./doc_Components/HomePage";






const Home =(props)=> {
  console.log("THE PROPS",props)
  const get_user_type_id = localStorage.getItem('user_type_id');
  const get_type = localStorage.getItem('user_type');
  // const [user_id,setUser_id] = useState(null)
  // useEffect(()=>{
  //   if(props.auth.token.user_type_id === get_user_type_id){

  //   }
  // },[props.auth.token.user_type_id])
  const PatOrDocHomePage = ()=>{
    console.log("THE FNUCTION GOT.....",get_type,get_user_type_id)
    if(get_type === 'PATIENT'){
      console.log("THE PAT GOT CAUGHT")
      return<PatHomePage/>
    }
    else if(get_type === 'DOCTOR')return<HomePage/>
    else return <></>
  }  

  
  
  return(
    <>
      <Jumbotron>
        <h1 className="display-3">Welcome {get_type}</h1>
        <p className="lead">
          This is a simple hero unit, a simple Jumbotron-style component for
          calling extra attention to featured content or information.
        </p>
        <hr className="my-2" />
        <p>
          It uses utility classes for typography and spacing to space
          content out within the larger container.
        </p>
        <p className="lead">
          <Button color="link">
            <Link to={`/stats/${get_user_type_id}`}>
              Check Stats
            </Link>
          </Button>
        </p>
      </Jumbotron>
      {PatOrDocHomePage()}
      {/* JSON.stringify */}
      {console.log("THE PROPS IN PATIENT",props)}
      
            
      </>
  )
}
  

const mapStateToProps = (state) => {
  return {
    auth: state.auth,
    // patient:state.pat_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  // fetchPatData: (pat_id) => dispatch(fetchPatData(pat_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(Home);
