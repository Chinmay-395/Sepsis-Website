import React from "react";
import { connect } from "react-redux";
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";
import { fetchPatData } from "../redux/ActionCreator";

class Graphvisulation extends React.Component {
  //I want to remove any sort of authentication inside this component
  //All the authentication stuff should be done prior
  //This component will also be used for Monitoring in real-time
  //__________ |Remove the authentication on this page ASAP| __________
  componentDidMount() {
    console.log("----", this.props);
    console.log(
      "user-type in props",
      typeof this.props.auth.token.user_type_id
    );
    console.log(
      "user-type in local",
      typeof localStorage.getItem("user_type_id")
    );
    this.props.fetchPatData(parseInt(this.props.patientId));
  }
  componentDidUpdate() {
    console.log(this.props.pat_data);
  }
  render() {
    return (
      <div style={{ padding: "15px" }}>
        <Container fluid>
          <Row>
            <div className="col-md-12 col-lg-6">
              <Card className="mb-3">
                <CardBody>
                  <CardTitle>Card-1</CardTitle>
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
