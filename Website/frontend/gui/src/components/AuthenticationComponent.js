import React, { Component } from 'react'
import { connect } from 'react-redux';
import { Redirect, /*Route*/ } from "react-router-dom";
import { authLogin, } from '../redux/ActionCreator'
import {
  Container, Col, Form,
  FormGroup, Label, Input,
  Button,
} from 'reactstrap';


class AuthenticationComponent extends Component {

  componentDidMount() {
    console.log("HEHI")
  }
  handleFormSubmit = () => {
    // preventDefault();
    console.log("EMail & password", this.email.value, this.password.value)
    this.props.authLogin(this.email.value, this.password.value)
  }


  render() {
    if (this.props.auth.token !== null) {
      return (
        <Redirect to="/" />
      )
    } else {
      return (
        <Container>
          <h2>Sign In</h2>
          <Form className="form">
            <Col>
              <FormGroup>
                <Label>Email</Label>
                <Input
                  type="email"
                  name="email"
                  id="exampleEmail"
                  placeholder="myemail@email.com"
                  innerRef={(input) => this.email = input}
                />
              </FormGroup>
            </Col>
            <Col>
              <FormGroup>
                <Label for="examplePassword">Password</Label>
                <Input
                  type="password"
                  name="password"
                  id="examplePassword"
                  placeholder="********"
                  innerRef={(input) => this.password = input}
                />
              </FormGroup>
            </Col>
            <Button onClick={() => this.handleFormSubmit()}>Submit</Button>
          </Form>
        </Container>
      )
    }

  }
}

const mapStateToProps = state => {
  return {
    auth: state.auth,
  }
}

const mapDispatchToProps = dispatch => ({
  authLogin: (username, password) => {
    dispatch(authLogin(username, password))
  }
})

export default connect(mapStateToProps, mapDispatchToProps)(AuthenticationComponent)
