import React, { Component } from 'react'
import { Redirect, Link } from 'react-router-dom'
import { connect } from 'react-redux'
import { Container, Row, Col, Card, CardBody, CardTitle } from "reactstrap";
// import { Link, withRouter } from 'react-router'
class Home extends Component {
  componentWillMount() {
    console.log("ALOHA from Home")
    console.log("PROPS>>>", this.props)
  }

  render() {
    return (
      <div>
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
    )
  }
}

const mapStateToProps = (state) => {
  return {
    auth: state.auth
  }
}
const mapDispatchToProps = dispatch => ({

})
export default connect(mapStateToProps, mapDispatchToProps)(Home)