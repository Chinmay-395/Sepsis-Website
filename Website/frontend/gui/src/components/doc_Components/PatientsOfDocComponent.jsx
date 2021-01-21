import React,{useState, useEffect} from 'react'
import { connect } from "react-redux";
import { useParams } from 'react-router-dom';
import { Button } from 'reactstrap';
import {fetchPatData} from "../../redux/ActionCreator";
import RenderPatientItem from "../pat_Components/PatHomePage"
/**[Patient's Details page]
 * This component is an details page of the patient
 * the patient list page is on the home-page for doctor
 */
function PatientsOfDocComponent(props) {
  let { pat_id } = useParams();
  console.log("THE ID of patient",pat_id)
  console.log("THE Porps in PATIENT DETAILS \n",props)
  /**This will only run once the component is mounted 
    rest of the time the new data would be fetched through "Fetch New Data" button
    though the onClick event
  */
  useEffect(()=>{
    console.log("THE USE-EFFECT of patient-detail component for doctor")
    props.fetchPatData(pat_id)
  },[])

  //initially will show table component
  const [tableOrGraph,setTableOrGraph] = useState(true)
  
  useEffect(() =>{
    console.log("THE LOCAL STATE",tableOrGraph)
  },[tableOrGraph])
  return (
    <div>
      <h1>HELLO TO PATIENTS OF DOCTOR</h1>
      <Button color="info" onClick={()=>setTableOrGraph(!tableOrGraph)}>{tableOrGraph?<>Graphs</>:<>Table</>}</Button><br/>
      <Button color="info" onClick={()=>props.fetchPatData(pat_id)}>Fetch New Data</Button><br/>
      <>
        {
        tableOrGraph?
        <>
          {props.patient_of_doc_data && <RenderPatientItem data={props.patient_of_doc_data.pat_data.sep_data}/>}
        </>:
        <>
          GRAPHS
        </>
        }
      </>
    </div>
  )
}
const mapStateToProps = (state) => {
  return {
    auth: state.auth,
    patient_of_doc_data: state.pat_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchPatData: (pat_id) => dispatch(fetchPatData(pat_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(PatientsOfDocComponent)
