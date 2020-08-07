import React from "react";
import { Table } from "reactstrap";
import { connect } from "react-redux";
import { Icon, Spin } from "antd";
import { Link } from "react-router-dom";
//custom imports
import { fetchDocData } from "../../redux/ActionCreator";
const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;

const RenderPatItem = (pat) => {
  console.log("The renderPatItem object", pat);
  console.log("The renderPatItem each object", pat.pat);

  return (
    <>
      <tr>
        <td>{pat.pat.iteration}</td>
        <td>{pat.pat.patient_id}</td>
        <td>
          <Link to={`/stats/${pat.pat.patient_id}`}>
            {pat.pat.patient_name}
          </Link>
        </td>
        <td>Stats need to be added</td>
      </tr>
    </>
  );
};

class HomePage extends React.Component {
  componentDidMount() {
    // sending the id of the doctor model
    // so as to fetch the particular doctor
    let doc_id = this.props.auth.token.user_type_id;
    console.log("THE DOCTOR ID THAT NEEDS TO BE SENT", doc_id);
    this.props.fetchDocData(doc_id);
    console.log("I RAN FIRST");
  }
  render() {
    console.log("NEW PROPS", this.props);

    if (this.props.doctor_data.isLoading || this.props.auth.loading) {
      return (
        <div className="container">
          <div className="row">
            <h3>Loading</h3>
            <Spin indicator={antIcon} />
          </div>
        </div>
      );
    } else {
      console.log("the props", this.props);
      const theArray = this.props.doctor_data.doc_data.each_pat_json;
      const docData = theArray.map((pat, index) => {
        console.log("RENDERPATITEM happens to be called", pat);
        console.log(index);
        pat.iteration = index + 1;
        console.log(pat);

        return (
          <>
            <RenderPatItem pat={pat} />
          </>
        );
      });
      return (
        <Table>
          <thead>
            <tr>
              <th>#</th>
              <th>ID</th>
              <th>Name</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>{docData}</tbody>
        </Table>
      );
    }
  }
}

const mapStateToProps = (state) => {
  console.log("THE STATE HAS SHIT", state);
  return {
    auth: state.auth,
    doctor_data: state.doc_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchDocData: (doc_id) => dispatch(fetchDocData(doc_id)),
});
export default connect(mapStateToProps, mapDispatchToProps)(HomePage);
