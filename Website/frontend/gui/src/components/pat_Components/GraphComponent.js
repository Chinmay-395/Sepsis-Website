import React from 'react'
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";

function Graphvisulation() {
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
  )
}
export default Graphvisulation