import React from "react";
import { Table } from "reactstrap";
import { connect } from "react-redux";
import { Icon, Spin } from "antd";
import { Link } from "react-router-dom";
//custom imports
import { fetchDocData } from "../../redux/ActionCreator";
const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;

// let url = "http://127.0.0.1:8000/sepsisAPI/patspat/";
function renderPatientStatsPage(val) {
  console.log("I RAN IN renderPatientStatsPage");
  console.log("The patient-ID", val);
}
const RenderPatItem = (pat) => {
  console.log("The renderPatItem object", pat);
  console.log("The renderPatItem each object", pat.pat);

  return (
    <>
      <tr>
        <td>{pat.pat.iteration}</td>
        <td>{pat.pat.patient_id}</td>
        <td onClick={() => renderPatientStatsPage(pat.pat.patient_id)}>
          <Link to="/stats">{pat.pat.patient_name}</Link>
        </td>
        <td>Stats need to be added</td>
      </tr>
    </>
  );
};

const HomePage = (props) => {
  console.log("NEW PROPS", props);
  if (props.doctor_data.isLoading) {
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
    console.log("the props", props);
    const theArray = props.doctor_data.doc_data.each_pat_json;
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

    console.log(theArray);
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
};

const mapStateToProps = (state) => {
  console.log("THE STATE HAS SHIT", state);
  return {
    auth: state.auth,
    doctor_data: state.doc_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchDocData: () => dispatch(fetchDocData()),
});
export default connect(mapStateToProps, mapDispatchToProps)(HomePage);
