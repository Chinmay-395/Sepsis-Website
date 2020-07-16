import React, { Component } from 'react'
import { Switch, Route, Redirect, withRouter } from 'react-router-dom'
import { connect } from 'react-redux';
import Home from './HomeComponent'
import AuthenticationComponent from './AuthenticationComponent'
class Main extends Component {
    componentDidMount() {
        console.log("componentDidMount ran inside Main ")
    }
    componentWillMount() {
        console.log("componentWillMount ran inside Main")
    }
    render() {
        console.log("Render method ran")
        return (
            <div>
                {/* Header component */}
                <Switch>
                    <Route path='/home' component={() => <Home />} />
                    <Route path='/login' component={() => <AuthenticationComponent />} />
                    <Redirect to='/home' />
                </Switch>
                {/* Footer component */}
            </div>
        )
    }
}
export default Main