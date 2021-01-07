import React from "react";
import { connect } from "react-redux";
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";
import {Line} from 'react-chartjs-2';

const simpleComp =(data)=> {
  console.log("THE CHART VALUES",data)
    Object.entries(data).forEach(([k,v]) => {
    console.log("The key: ",k)
    console.log("The value: ",v)
    })

    let chart_prop = {
      labels: [0,20,40,60,80,100,120,140,160,180,200],
      datasets: [
        {
          label: "level of thick",
          data: data['heart_rate'],//[32,45,12,76,69],
          backgroundColor: ["rgba(75, 192, 192, 0.6)"],
          borderWidth: 4
        }
      ]
    }
    return(
    <div>
      <Line data={chart_prop} options={{responsive:true}} />
    </div>
    )
  
  
  // ,width:"500px"
  //style={{height:"500px"}}
  // return(
  //  <>{each_sepsis_prop}</> 
  // )
}
//create a useEffect that will fetch all the values on refresh
function Graphvisulation(props) {
  console.log("GRAPH",props.pat_data.pat_data.sep_data)
  var chart_data = props.pat_data.pat_data.sep_data
  /**[Note]
   * Since the data coming in this component is through props
   * which has alread reversed data inside it, from the home_component;
   * so no need to reverse it again.
   */

  let obj_data = {
    "heart_rate":[],
    "oxy_saturation":[],
    "temperature":[],
    "blood_pressure":[],
    "mean_art_pre":[],
    "resp_rate":[]
  }
  
  for(var i=0; i<10;i++){
    obj_data["heart_rate"].push(chart_data[i]['heart_rate'])
    obj_data['oxy_saturation'].push(chart_data[i]['oxy_saturation'])
    obj_data['temperature'].push(chart_data[i]['temperature'])
    obj_data['blood_pressure'].push(chart_data[i]['blood_pressure'])
    obj_data['mean_art_pre'].push(chart_data[i]['mean_art_pre'])
    obj_data['resp_rate'].push(chart_data[i]['resp_rate'])
  }
  
  console.log("**********************",obj_data)
  return(
    <>{simpleComp(obj_data)}</>
  )
}
const mapStateToProps = (state) => {
  // console.log("THE STATE HAS ", state);
  return {
    auth: state.auth,
    pat_data: state.pat_data,
  };
};
const mapDispatchToProps = (dispatch) => ({
});
export default connect(mapStateToProps, mapDispatchToProps)(Graphvisulation);

{/* <Card className="mb-3">
        <CardBody >
          <CardTitle>Card-12</CardTitle>
          <Line data={chart_prop} options={{responsive:true}} />
        </CardBody>
      </Card> */}