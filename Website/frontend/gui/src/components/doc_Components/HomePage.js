import React from "react";
import { Table } from "reactstrap";
import { connect } from "react-redux";
import { Icon, Spin } from "antd";

//custom imports
import { fetchDocData } from "../../redux/ActionCreator";

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;

const RenderPatItem = (pat) => {
  console.log("The renderPatItem object", pat);
  console.log("The renderPatItem each object", pat.pat);
  // console.log(pat.pat.patient_id);
  // const iteration_number = pat.pat;
  // console.log("The walking dead", iteration_number);

  return (
    <>
      <tr>
        <td>{pat.pat.iteration}</td>
        <td>{pat.pat.patient_id}</td>
        <td>{pat.pat.patient_name}</td>
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
  return {
    auth: state.auth,
    doctor_data: state.doc_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
  fetchDocData: () => dispatch(fetchDocData()),
});
export default connect(mapStateToProps, mapDispatchToProps)(HomePage);
