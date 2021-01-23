import React,{useEffect,useState} from "react";
import { connect } from "react-redux";
import {Bar} from 'react-chartjs-2';
import {connect_ws, messages} from "../hooks/socketConnection"
//**************************These attribute functions for graphs **************************/
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
// let socket; 
// export const connectSocket = () => {
//   console.log("I RAN IN connectSocket func")
//   if (!socket || socket.closed) {
//     console.log("I ONLY RUN ONCE")
//     socket = new WebSocket(`ws://localhost:8000/sepsisDynamic/?token=${localStorage.getItem('token')}`);
//   }
// };
//***************************************************end of This is related to socket connection ****************************************************/
// let socket = new WebSocket(`ws://localhost:8000/sepsisDynamic/?token=${localStorage.getItem('token')}`);
function GraphDynamicComponent(props) {
  // connectSocket()
  console.log("GRAPH",props)
  const [sepsis_data, setSepsis_data] = useState(genData())
  
  
  useEffect(()=>{
    console.log("THE USE-EFFECT HOOK RAN")
    connect_ws()

    const subscription = messages.subscribe((message)=>{
      console.log("MESSAGE in graph \n",message)
      setSepsis_data(genData(message))
    })
    return () => {
      if (subscription) {
        subscription.unsubscribe();
      }
    }

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