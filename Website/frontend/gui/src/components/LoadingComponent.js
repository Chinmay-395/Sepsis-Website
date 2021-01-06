import React from 'react'
import { Icon, Spin } from "antd";

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;

function LoadingComponent() {
  return (
    <div className="container">
      <div className="row">
        <h3>Loading</h3>
        <Spin indicator={antIcon} />
      </div>
    </div>
  )
}

export default LoadingComponent
