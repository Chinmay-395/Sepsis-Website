import React from "react";
import { connect } from "react-redux";
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";
import { fetchPatData } from "../redux/ActionCreator";

function Graphvisulation(props) {
  //I want to remove any sort of authentication inside this component
  //All the authentication stuff should be done prior
  //This component will also be used for Monitoring in real-time
  //__________ |Remove the authentication on this page ASAP| __________
  console.log("GRAPH",props)

  // useEffect(()=>{
  //   console.log("THE PROPS IN useEffectHOOK",props)
  //   props.fetchPatData(localStorage.getItem('user_type_id'))
  // },[]);

  const simpleComp =(
    {
      blood_pressure,
      heart_rate,
      mean_art_pre,
      oxy_saturation,
      resp_rate,
      temperature
    })=> (
    <div className="col-md-12 col-lg-6">
              <Card className="mb-3">
                <CardBody>
                  <CardTitle>Card-12</CardTitle>
                </CardBody>
              </Card>
    </div>
  )
  
  

    return (
      <div style={{ padding: "15px" }}>
        <Container fluid>
          <Row>
            <div className="col-md-12 col-lg-6">
              <Card className="mb-3">
                <CardBody>
                  <CardTitle>Card-12</CardTitle>
                </CardBody>
              </Card>
            </div>
            <div className="col-md-12 col-lg-6">
              <Row>
                <div className="col-md-6">
                  <Card className="mb-3">
                    <CardBody>
                      <CardTitle>Card-1</CardTitle>
                    </CardBody>
                  </Card>
                </div>
                <div className="col-md-6">
                  <Card className="mb-3">
                    <CardBody>
                      <CardTitle>Card-1</CardTitle>
                    </CardBody>
                  </Card>
                </div>
                <div className="col-md-6">
                  <Card className="mb-3">
                    <CardBody>
                      <CardTitle>Card-1</CardTitle>
                    </CardBody>
                  </Card>
                </div>
                <div className="col-md-6">
                  <Card className="mb-3">
                    <CardBody>
                      <CardTitle>Card-1</CardTitle>
                    </CardBody>
                  </Card>
                </div>
              </Row>
            </div>
          </Row>
        </Container>
      </div>
    );
  }

const mapStateToProps = (state) => {
  // console.log("THE STATE HAS ", state);
  return {
    auth: state.auth,
    pat_data: state.pat_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchPatData: (pat_id) => dispatch(fetchPatData(pat_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(Graphvisulation);
