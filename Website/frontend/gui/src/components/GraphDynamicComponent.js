import React, {useEffect} from "react";
import { connect } from "react-redux";
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";
import { fetchPatData } from "../redux/ActionCreator";

function GraphDynamicComponent(props) {
  //I want to remove any sort of authentication inside this component
  //All the authentication stuff should be done prior
  //This component will also be used for Monitoring in real-time
  //__________ |Remove the authentication on this page ASAP| __________
  console.log("GRAPH",props)

  // useEffect(()=>{
  //   console.log("THE PROPS IN useEffectHOOK",props)
  //   props.fetchPatData(localStorage.getItem('user_type_id'))
  // },[]);

  /**[What exactly I will be using this component for] 
   * The <patient_data> will be an array of json data that would be from WebSocket 
  */
  const get_user_type_id = localStorage.getItem('user_type_id')
  const patient_data = ["Heart Rate", "O2 Sats", "temperature","blood pressure","respiratory rate","mean artery pressure"] 
  const simpleComp =(patient_data,index)=> {
    console.log("THE INDEX AND PATIENT_DATA",index,patient_data)
    /**[Can be used in key for unique div]
     * get_user_type_id.toString() + "-patient-" + key={index.toString()}
     */
    return(
      
    <div className="col-md-12 col-lg-12">
      <Card className="mt-3">
        <CardBody>
          <CardTitle>{patient_data}</CardTitle>
        </CardBody>
      </Card>
    </div>
  )}
  
  

    return (
      <Container fluid>
        <Row>
          {patient_data.map((sep_data,index) => 
            <React.Fragment key={index}>
              {simpleComp(sep_data,index)}
            </React.Fragment>
            )
          }
        </Row>
      </Container>
    )
}

const mapStateToProps = (state) => {
  // console.log("THE STATE HAS ", state);
  return {
    auth: state.auth,
    // pat_data: state.pat_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  // fetchPatData: (pat_id) => dispatch(fetchPatData(pat_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(GraphDynamicComponent);
