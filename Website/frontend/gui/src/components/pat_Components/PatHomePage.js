import React,{useEffect} from "react";
import { connect } from "react-redux";
//reactStrap
import { Table } from "reactstrap";
//components import
import LoadingComponent from "../LoadingComponent"
//redux imports
import {fetchPatData} from "../../redux/ActionCreator";

const get_user_type_id = localStorage.getItem('user_type_id');

function TabulatedData(values){
  return (
        <Table>
          <thead>
            <tr>
              <th>#</th>
              <th>ID</th>
              <th>Name</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody></tbody>
        </Table>
      );
}

function RenderPatientItem({data}){
  console.log("THE ARRAY",data)
  return (
    <h1>It works</h1>
  )
}

function PatHomePage(props) {
  console.log("PROPS PROPS IN PATHOMEPAGE",props)
  useEffect(() => {
    console.log("THE UseEffct ran")
    props.fetchPatData(get_user_type_id)
    console.log("WHEN DATA IS MOUNTED",props)
  },[])

  console.log("PROPS PROPS IN PATHOMEPAGE right after useEffect \n \n",props)
  if(props.patient_data.isLoading)return(<LoadingComponent/>)
  else if(props.patient_data.pat_data !==null){
    console.log("THE ARRAY OUTSIDE ARROW FUNC",props.patient_data.pat_data.sep_data);
    const theArray = props.patient_data.pat_data.sep_data
    // RenderPatientItem(theArray)
    return(
    <>
      <h1>THE ARROW FUNC</h1>
      {<RenderPatientItem data={theArray}/>}
    </>
    )
  }else{

      return (
        <>
        <h1>NOTHING IS RETURNING</h1>
        </>
      );
    }
  }


const mapStateToProps = (state) => {
  console.log("THE STATE HAS SHIT", state);
  return {
    auth: state.auth,
    patient_data: state.pat_data,//{ isLoading: false },
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchPatData: (pat_id) => dispatch(fetchPatData(pat_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(PatHomePage);

// const theArray = this.props.doctor_data.doc_data.each_pat_json;