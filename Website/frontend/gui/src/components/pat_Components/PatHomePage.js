import React,{useEffect} from "react";
import { connect } from "react-redux";
//reactStrap
import { Table } from "reactstrap";
//components import
import LoadingComponent from "../LoadingComponent"
//redux imports
import {fetchPatData} from "../../redux/ActionCreator";

export function RenderPatientItem({data}){
  if(data!=null || data!==undefined){
    const rev_array = data
    // console.log("THE REVERSE VALUE THAT SHOULD BE COMPARED \n \n",rev_array.reverse().slice(0,5))
    const returnThis = data.reverse().slice(0,10).map((obj,index)=> {
      return(
        <tbody key={index}>
          <tr>
            <td>{index+1}</td>
            <td>{obj.heart_rate}</td>
            <td>{obj.oxy_saturation}</td>
            <td>{obj.temperature}</td>
            <td>{obj.blood_pressure}</td>
            <td>{obj.mean_art_pre}</td>
            <td>{obj.resp_rate}</td>
          </tr>
        </tbody>
      )
    });
    return (
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>Heart Rate</th>
            <th>Oxy Saturation</th>
            <th>temperature</th>
            <th>blood Pressure</th>
            <th>Mean Artial Pressure</th>
            <th>Respiratory Rate</th>
          </tr>
        </thead>
        {returnThis}
      </Table>
    )
  }
  else {return(<></>)}
}

function PatHomePage(props) {
  /**Home-page and patient-detail-page */
  console.log("PRops in pat", props)
  /**The following useEffect will only when the patient's auth token & pat_id is changed */
  useEffect(() => {
    props.fetchPatData(props.auth.token.user_type_id)
  },[props.auth.token.user_type_id])

  if (props.patient_data.isLoading)return(<LoadingComponent/>)
  else if(props.patient_data.pat_data !==null && props.patient_data.pat_data.sep_data){
    const theArray = props.patient_data.pat_data.sep_data
    return(
    <>
      <h2>The Latest value of sepsis</h2>
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
    patient_data: state.pat_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchPatData: (pat_id) => dispatch(fetchPatData(pat_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(PatHomePage);
