import React from "react";
import { connect } from "react-redux";
import { Icon, Spin } from "antd";
import { Link } from "react-router-dom";
import { Jumbotron, Button } from "reactstrap";
//custom imports
// import { fetchDocData } from "../../redux/ActionCreator";

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;

function PatHomePage(props) {
  // render() {
    // console.log("NEW PROPS", props);

    if (props.patient_data.isLoading) {
      console.log("I ran");
      return (
        <div className="container">
          <div className="row">
            <h3>Loading</h3>
            <Spin indicator={antIcon} />
          </div>
        </div>
      );
    } else {
      return (
        <>
          <Jumbotron>
            <h1 className="display-3">Hello, world!</h1>
            <p className="lead">
              This is a simple hero unit, a simple Jumbotron-style component for
              calling extra attention to featured content or information.
            </p>
            <hr className="my-2" />
            <p>
              It uses utility classes for typography and spacing to space
              content out within the larger container.
            </p>
            <p className="lead">
              <Button color="link">
                <Link to={`/stats/${props.auth.token.user_type_id}`}>
                  Check Stats
                </Link>
              </Button>
            </p>
          </Jumbotron>
        </>
      );
    }
  }
// }

const mapStateToProps = (state) => {
  console.log("THE STATE HAS SHIT", state);
  return {
    auth: state.auth,
    patient_data: { isLoading: false },
  };
};
const mapDispatchToProps = (dispatch) => ({
  // fetchDocData: () => dispatch(fetchDocData()),
});
export default connect(mapStateToProps, mapDispatchToProps)(PatHomePage);
