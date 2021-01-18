import React,{useEffect,useState} from "react";
import { connect } from "react-redux";
import { Container, Row, /*Col,*/ Card, CardBody, CardTitle } from "reactstrap";
import { webSocket } from 'rxjs/webSocket';
import { share } from 'rxjs/operators';
/** We don't need the below import; this component will run through RxJs*/
// import { fetchPatData } from "../redux/ActionCreator";
import {Bar, Line} from 'react-chartjs-2';



// const patient_data = {"heart_rate":56, "oxy_saturation":98, "temperature":75,"blood_pressure":15,"resp_rate":21,"mean_art_pre":35}
const genData = (patient_data) => {
  if(patient_data!==undefined){
    // console.log("THE DATA in genData",patient_data)
    // console.log("*******--------*******--------",patient_data.blood_pressure)

    return({
    labels: ['Heart Rate', 'O2 Sats', 'temperature', 'blood pressure', 'respiratory rate', 'mean artery pressure'],
    datasets: [
      {
        label: 'Dynamic Sepsis Data',
        data: [
          patient_data['blood_pressure'],
          patient_data['heart_rate'],
          patient_data['mean_art_pre'],
          patient_data['oxy_saturation'],
          patient_data['resp_rate'],
          patient_data['temperature']
        ],
        backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 4,
      },
    ],
  })
  }else{
    return({
    labels: ['Heart Rate', 'O2 Sats', 'temperature', 'blood pressure', 'respiratory rate', 'mean artery pressure'],
    datasets: [
      {
        label: 'Dynamic Sepsis Data',
        data: [0,0,0,0,0,0],
        backgroundColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 4,
      },
    ],
  }) 
  }
}

const options = {
  scales: {
    yAxes: [
      {
        ticks: {
          beginAtZero: true,
        },
      },
    ],
  },
}
//***************************************************This is related to socket connection ****************************************************/
// let _socket; 
// export let messages; 

// export const connectSocket = () => {
//   console.log("I RAN IN connectSocket func")
//   if (!_socket || _socket.closed) {
//     console.log("I ONLY RUN ONCE")
//     const token = localStorage.getItem('token');
//     _socket = webSocket(`ws://localhost:8000/sepsisDynamic/?token=${token}`);
//     messages = _socket.pipe(share());
//     messages.subscribe(message => console.log(message));
//   }
// };
//***************************************************end of This is related to socket connection ****************************************************/
let socket = new WebSocket(`ws://localhost:8000/sepsisDynamic/?token=${localStorage.getItem('token')}`);
function GraphDynamicComponent(props) {
  // connectSocket()
  console.log("GRAPH",props)
  const [sepsis_data, setSepsis_data] = useState(genData())
  
  
  useEffect(()=>{
      
      const interval = setInterval(() => {
        
        socket.onmessage = function(event) {
        console.log(`[message] Data received from server: ${event.data}`);
        
        setSepsis_data(genData(JSON.parse(event.data)))
        console.log("THE USE EFFECR")
        };
    }, 5000)

    return () => clearInterval(interval)
  },[]);

  return (
    <>
      <div >
        {/* style={{ position:"relative", width:500, height:300 }} */}
        <Bar data={sepsis_data} options={options} />
      </div>
    </>
  )
}

const mapStateToProps = (state) => {
  return {
    auth: state.auth,
  };
};
const mapDispatchToProps = (dispatch) => ({
});
export default connect(mapStateToProps, mapDispatchToProps)(GraphDynamicComponent);