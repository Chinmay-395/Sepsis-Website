import React, { useEffect } from "react";
import { Table } from "reactstrap";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
//custom imports
import { fetchDocData } from "../../redux/ActionCreator";
import LoadingComponent from "../LoadingComponent";


function FetchPatsOfDoc({data}){
  if(data!==null && data !==undefined){
    console.log("THE DATA OF DOCTOR",data)
    const tbodyOfPatient = data.map((obj,index)=>{
      return (
        <tr key={index}>
          <td>{index + 1}</td>
          <td>{obj.patient_id}</td>
          <td>
            <Link to={`/patient/${obj.patient_id}`}>
              {obj.patient_name}
            </Link>
          </td>
          <td>Stats need to be added</td>
        </tr>
      );
    })
    return (
      <>
          <Table>
            <thead>
              <tr> 
                <th>#</th> 
                <th>ID</th> 
                <th>Name</th> 
                <th>Status</th> 
              </tr> 
            </thead> 
            <tbody>
            {tbodyOfPatient}
            </tbody>
          </Table>
      </>
    );
  }else return <></>
}

function HomePage(props) {
    console.log("NEW PROPS", props);
  /**The following useEffect will run on every render of Doctor's Home-Page  
   * Which will give us all the patient's pertaining to the doctor, pat_id and status
  */
    useEffect(()=>{
    let doc_id = props.auth.token.user_type_id;
    console.log("THE DOCTOR ID THAT NEEDS TO BE SENT", doc_id);
    props.fetchDocData(doc_id);
    console.log("I RAN FIRST");
  },[props.auth.token.user_type_id])
  
  
  

    if (props.doctor_data.isLoading)return<LoadingComponent/>
    else if(props.doctor_data.doc_data !== null) {
      const theArray = props.doctor_data.doc_data.each_pat_json;
      return <FetchPatsOfDoc data={theArray} />
    }
    else{
      return (
        <>
        <h1>NOTHING IS RETURNING in Doctor</h1>
        </>
      );
    }
    
}

const mapStateToProps = (state) => {
  console.log("THE STATE HAS SHIT", state);
  return {
    auth: state.auth,
    doctor_data: state.doc_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchDocData: (doc_id) => dispatch(fetchDocData(doc_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(HomePage);


