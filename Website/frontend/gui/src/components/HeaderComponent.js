import React, { Component } from "react";
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  // NavbarText,
} from "reactstrap";
import { connect } from "react-redux";
import { logout } from "../redux/ActionCreator";
import { Link } from "react-router-dom";

const links = [
  { key: "1", href: "/home", text: "Home" },
  { key: "2", href: "/stats", text: "stats" },
  { key: "3", href: "/monitor", text:"Monitoring" },
  { key: "4", href: "/login", text: "LOGIN" },
];

class Header extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isOpen: false,
    };

    this.toggle = this.toggle.bind(this);
  }
  logoutbutton = () => {
    this.props.logout();
  };

  toggle() {
    this.setState({
      isOpen: !this.state.isOpen,
    });
  }
  createNavItem = ({ href, text, key }) => {
    if (this.props.auth.token !== null) {
      console.log("the email", localStorage.getItem('email'))
      console.log("The text", text)
      if (text === "LOGIN") {
        return (
          <React.Fragment key={key}>
            <NavItem >
              <Link to="#" className='nav-link'>{localStorage.getItem("email")}</Link>
            </NavItem>
            <button onClick={() => this.logoutbutton()}>Logout</button>
          </React.Fragment>
          
        );
      }else if(text==="Monitoring"){
        // href = `${href}${}`
        var new_href = `${href}/${localStorage.getItem("user_type_id")}/`
        // console.log("Href of stats",href,new_href)
        return (
          
            <NavItem key={key}>
              <Link to={new_href} className="nav-link">{text}</Link>
            </NavItem>
          
        );
      }else if(text==="stats"){
        var diff_href = `${href}/${localStorage.getItem("user_type_id")}/`
        // console.log("Href",href,new_href)
        return (
          
            <NavItem key={key}>
              <Link to={diff_href} className="nav-link">{text}</Link>
            </NavItem>
          
        );
      }
      else {
        return (
          <NavItem key={key}>
            <NavLink href={href}>
              {text}
            </NavLink>
          </NavItem>
        );
      }
    } else {
      return (
        <NavItem key={key}>
          <NavLink href={href}>
            {text}
          </NavLink>
        </NavItem>
      );
    }
  };
  render() {
    console.log("props in header is>>>", this.props)
    return (
      <div>
        <Navbar color="light" light expand="md">
          <NavbarBrand href="/">Sepsis Diagnostic System</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              {links.map(this.createNavItem)}
            </Nav>
          </Collapse>
        </Navbar>
      </div>
    );
  }
}
const mapStateToProps = (state) => {
  return {
    auth: state.auth,
  };
};
const mapDispatchToProps = (dispatch) => ({
  logout: () => {
    dispatch(logout());
  },
});
export default connect(mapStateToProps, mapDispatchToProps)(Header);


// className={className}
// const linkFunc = () => (
//   <>
//   <NavItem>
//     <NavLink href="/home" >
//       Home
//     </NavLink>
//   </NavItem>
//   <NavItem>
//     <NavLink href="/home" >
//       Home
//     </NavLink>
//   </NavItem>
//   <NavItem>
//     <NavLink href="/home" >
//       Home
//     </NavLink>
//   </NavItem>
//   <NavItem>
//     <NavLink href="/home" >
//       Home
//     </NavLink>
//   </NavItem>
//   </>
// )
