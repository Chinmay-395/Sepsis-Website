import React, { Component } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  // NavbarText,
} from 'reactstrap';
import { connect } from 'react-redux'

const links = [
  { key: '1', href: '/home', text: 'Home' },
  { key: '2', href: '#card', text: 'Profile' },
  { key: '3', href: '#about', text: 'Monitoring' },
  { key: '4', href: '/login', text: 'LOGIN' },
];



class Header extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isOpen: false
    };

    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  createNavItem = ({ href, text, className, key }) => {
    if (this.props.auth.token !== null) {
      // console.log("the email", localStorage.getItem('email'))
      // console.log("The text", text)
      if (text === 'LOGIN') {
        return (
          <>
            <NavItem key={key}>
              <NavLink href="#">{localStorage.getItem('email')}</NavLink>
            </NavItem>
            {/* <NavItem key={key + 1}>
              <NavLink href="#">Logout</NavLink>
            </NavItem> */}
          </>
        )

      }
      else {
        return (
          <NavItem key={key}>
            <NavLink href={href} className={className}>{text}</NavLink>
          </NavItem>
        )
      }
    } else {
      return (
        <NavItem key={key}>
          <NavLink href={href} className={className}>{text}</NavLink>
        </NavItem>
      )
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
    auth: state.auth
  }
}
const mapDispatchToProps = dispatch => ({

})
export default connect(mapStateToProps, mapDispatchToProps)(Header)