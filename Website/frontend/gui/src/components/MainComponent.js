import React, { Component } from 'react'
import { Switch, Route, Redirect, withRouter } from 'react-router-dom'
import { connect } from 'react-redux';
import Home from './HomeComponent'
import AuthenticationComponent from './AuthenticationComponent'
import Header from './HeaderComponent'

class Main extends Component {
    componentDidMount() {
        console.log("componentDidMount ran inside Main ")

        if (this.props.auth.token == null) {
            console.log("You lost your props JACK")

        } else {
            console.log(">>>>", this.props)
        }
    }
    componentDidUpdate() {
        console.log("componentUdate>>>>", this.props)
    }
    render() {

        return (
            <div>
                <Header />
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
const mapStateToProps = (state) => {
    return {
        auth: state.auth
    }
}
const mapDispatchToProps = dispatch => ({

})
export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Main))