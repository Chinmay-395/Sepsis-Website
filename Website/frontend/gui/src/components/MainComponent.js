import React, { Component } from 'react'
import { Switch, Route, Redirect, withRouter } from 'react-router-dom'
import { connect } from 'react-redux';
import Home from './HomeComponent'
import AuthenticationComponent from './AuthenticationComponent'


class Main extends Component {
    componentDidMount() {
        console.log("componentDidMount ran inside Main ")

        if (this.props.auth.token == null || this.props == undefined) {
            console.log("You lost your props JACK")
            // alert("You lost your props JACK")         

        } else {
            console.log(">>>>", this.props)
        }
    }

    render() {
        if (this.props.auth.token == null || this.props == undefined) {
            return (
                <Route path='/login' component={() => <AuthenticationComponent />} />
            )

        } else {
            return (
                <div>
                    {/* Header component */}
                    <Switch>
                        <Route path='/home' component={() => <Home />} />
                        <Redirect to='/home' />
                    </Switch>
                    {/* Footer component */}
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
// const mapDispatchToProps = dispatch => ({

// })
export default withRouter(connect(mapStateToProps)(Main))