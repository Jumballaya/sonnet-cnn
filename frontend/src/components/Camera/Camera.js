import React, { Component } from 'react';
import { Camera } from '../../utils/images';
import './camera.css';

class CameraComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      takingPic: false,
    };
    this.camera = new Camera(window.innerWidth, window.innerHeight);
    this.camera.activateCamera();
    this.handleTakePic = this.handleTakePic.bind(this);
    this.handleInitVideo = this.handleInitVideo.bind(this);
  }

  handleTakePic(e) {
    e.preventDefault();
    this.camera.capture().then(img => this.props.handleImage(img));
    this.setState({
      takingPic: false,
    });
  }

  handleInitVideo(e) {
    e.preventDefault();
    this.setState({ takingPic: true });
  }

  renderVideo() {
    const h = window.innerHeight;
    const w = window.innerWidth;
    return (
      <video
        width={`${w}px`}
        height={`${h}px`}
        ref={ref => {
          this.video = ref;
          if (ref) {
            ref.srcObject = this.camera.stream;
            ref.play();
          }
        }}
        onClick={this.handleTakePic}
        className="video--fullscreen"
      />
    );
  }

  renderButton() {
    return <button onClick={this.handleInitVideo}>Take Photo</button>;
  }

  render() {
    const { takingPic } = this.state;
    return takingPic ? this.renderVideo() : this.renderButton();
  }
}

export default CameraComponent;
