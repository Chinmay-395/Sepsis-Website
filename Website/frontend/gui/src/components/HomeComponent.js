import React, { Component } from 'react'
import { Redirect, Link } from 'react-router-dom'
// import { Link, withRouter } from 'react-router'
class Home extends Component {
    componentWillMount() {
        console.log("ALOHA from Home")
        console.log("PROPS>>>", this.prop)
    }
    handleClick = () => {
        console.log("VOILA")

    }
    render() {
        return (
            <div>
                <p>The Landing Page of the website</p>
                <button onClick={() => this.handleClick()} >Click me</button>
                <br />
                <Link to="/login">Click to login</Link>
            </div >
        )
    }
}
export default Home