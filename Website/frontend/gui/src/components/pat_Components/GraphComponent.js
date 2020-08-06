import React from "react";
import { connect } from "react-redux";
import { Link, useLocation } from "react-router-dom";
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";

class Graphvisulation extends React.Component {
  componentWillMount() {
    console.log("----", this.props);
    console.log(this.props.location);
    // let location = useLocation();
    // console.log(location);
  }
  componentDidUpdate() {
    console.log("----", this.props);
  }
  render() {
    console.log("GRAPH PROPS", this.props);
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
  console.log("THE STATE HAS ", state);
  return {
    auth: state.auth,
  };
};
const mapDispatchToProps = (dispatch) => ({
  // fetchDocData: () => dispatch(fetchDocData()),
});
export default connect(mapStateToProps, mapDispatchToProps)(Graphvisulation);
