import React from 'react';
import { Table } from 'reactstrap';
import { connect } from 'react-redux'
//custom imports
import { fetchDocData } from '../../redux/ActionCreator'

// class PatientsTable extends React.Component {
//   componentWillMount() {
//     console.log("THE DOC's Patient-Table ----->", this.props)

//   }
// componentDidMount() {
//   console.log("THE DOC's Patient-Table ----->", this.props)
// }

// componentDidUpdate() {
//   console.log("THE DOC's Patient-Table ----->", this.props)
//   console.log("Patient information ==========>", this.props.props.doc_data)
// }
// render() {
// }
const PatientsTable = (props) => {
  console.log("The info", props)
  return (
    <Table>
      <thead>
        <tr>
          <th>#</th>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Username</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Larry</td>
          <td>the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody>
    </Table >
  )
}





const HomePage = (props) => {
  console.log("THE DOC's HomePage ----->", props)
  return (
    <PatientsTable info={props.doctor_data} />
  );
}


const mapStateToProps = (state) => {
  return {
    auth: state.auth,
    doctor_data: state.doc_data
  }
}
const mapDispatchToProps = dispatch => ({
  fetchDocData: () => dispatch(fetchDocData())
})
export default connect(mapStateToProps, mapDispatchToProps)(HomePage)