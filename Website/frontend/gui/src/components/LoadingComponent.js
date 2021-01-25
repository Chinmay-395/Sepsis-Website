import React from 'react'
import { Spinner } from 'reactstrap';


const LoadingComponent = ()=> {
  return (
    <div className="container">
      <Spinner color="primary" />
    </div>
  )
}

export default LoadingComponent
