import React, { Component } from 'react'
// import { Redirect, Link } from 'react-router-dom'
// import { Link, withRouter } from 'react-router'

import { connect } from 'react-redux'
import Graphvisulation from './GraphComponent'

class Home extends Component {
  componentWillMount() {
    console.log("ALOHA from Home")
    console.log("PROPS>>>", this.props)
  }
  componentDidUpdate() {
    console.log("***************WE ARE*********")
  }

  render() {
    console.log('THE USER IS A', localStorage.getItem('user_type'))
    if (localStorage.getItem('user_type') === 'DOCTOR') {
      return (
        <div>
          <h1>Hello Doctor</h1>
        </div>
      )
    }
    else if (localStorage.getItem('user_type') === 'PATIENT') {
      return (
        <Graphvisulation />
      )
    }
    else {
      return (
        <div>
          <h1>You aren't suppose to be here</h1>
        </div>
      )
    }

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