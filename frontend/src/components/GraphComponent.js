import React, { useEffect, useState } from "react";
import { connect } from "react-redux";
// import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";
import {Line} from 'react-chartjs-2';
import { useParams } from "react-router-dom";
import LoadingComponent from "./LoadingComponent";

function simpleComp(data){
  let chart_prop =Object.entries(data).map(([k,v],index) => {
    var chart_val = {
        labels: [0,20,40,60,80,100,120,140,160,180,200],
        datasets: [
          {
            label:k,
            data: v,
            backgroundColor: ["rgba(75, 192, 192, 0.6)"],
            borderWidth: 4
          }
        ]
      }
    return(
      <div key={index} >
        {/* style={{ position:"relative", width:500, height:300, alignContent:"center" }} */}
        <Line data={chart_val} options={{responsive:true}} />
      </div>
      
    )
  })
  return chart_prop
}


//create a useEffect that will fetch all the values on refresh
function Graphvisulation(props) {
  let { pat_id } = useParams();
  console.log("THE ID of patient",pat_id)
  console.log("PROPS in GRAPH Component",props)
  var chart_data = props.pat_data.pat_data.sep_data
  chart_data = chart_data.reverse()
  /**[Note]
   Since the data coming in this component is through props
   which has alread reversed data inside it, from the home_component;
   so no need to reverse it again.
   */
  const [graph, setGraph] = useState(null)
  const [loading,setLoading] = useState(true)

  
  
  useEffect(()=>{
    console.log("I RAN in useEFFCET")
    let obj_data = {
        "heart_rate":[],
        "oxy_saturation":[],
        "temperature":[],
        "blood_pressure":[],
        "mean_art_pre":[],
        "resp_rate":[]
      }
    setGraph(()=>{
      console.log("I RAN in setGraphs")
      
      for(var i=0; i<10;i++){
        obj_data["heart_rate"].push(chart_data[i]['heart_rate'])
        obj_data['oxy_saturation'].push(chart_data[i]['oxy_saturation'])
        obj_data['temperature'].push(chart_data[i]['temperature'])
        obj_data['blood_pressure'].push(chart_data[i]['blood_pressure'])
        obj_data['mean_art_pre'].push(chart_data[i]['mean_art_pre'])
        obj_data['resp_rate'].push(chart_data[i]['resp_rate'])
      }
      return obj_data
    })
    setLoading(false)
    
    return ()=>{}
  },[chart_data])
  
  
  
  console.log("THE graph VAls of local-state are",graph)
  return(
    <>{loading?<LoadingComponent/>:simpleComp(graph)}</>
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

