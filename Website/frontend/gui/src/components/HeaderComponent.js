import React, { useState } from "react";
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
import { Link, Redirect } from "react-router-dom";


function Header(props){
  console.log("THE PROPS in header",props)
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);
 
  
  const logoutbutton = () => {
    props.logout();
  };
  const NavBarWhenLoggedIn = () => {
    return (
      <>
        <NavItem>
          <Link to={`/stats/${localStorage.getItem("user_type_id")}`} className="nav-link">stats</Link>
        </NavItem>
        <NavItem>
          <Link to={`/monitor/${localStorage.getItem("user_type_id")}`} className="nav-link">Monitoring</Link>
        </NavItem>
        <NavItem >
          <Link to="#" className='nav-link'>{localStorage.getItem("email")}</Link>
        </NavItem>
        <button onClick={logoutbutton}>Logout</button>
      </>
      );
  }
  if(props.auth.token==null){
    return(<Redirect to="/"/>)
  }
  return (
    <div>
      <Navbar color="light" light expand="md">
        <NavbarBrand href="/">Sepsis Diagnostic System</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="ml-auto" navbar>
            {props.auth.token!==null?<NavBarWhenLoggedIn/>:<></>}
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
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