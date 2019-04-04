import React from 'react';
import { connect } from 'react-redux';
import { Grid } from 'grommet';
import { fetchImagenet } from '../store/actions/imagenet';
import API from '../api/imagenet';
import ImageCard from '../components/ImageCard/ImageCard';
import CameraComponent from '../components/Camera/Camera';

class Imagenet extends React.Component {
  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleImg = this.handleImg.bind(this);
  }

  handleSubmit(e) {
    e.preventDefault();
    const files = Array.from(e.target.files);
    files.map(img => this.props.getImagenet(img));
  }

  renderImages() {
    const key = name => (name || 'image-card') + Math.random() + Date.now();
    return this.props.images
      .reverse()
      .map(img => <ImageCard {...img} key={key(img.data.name)} />);
  }

  handleImg(img) {
    this.props.getImagenet(img);
  }

  render() {
    const mobile =
      typeof window.orientation !== 'undefined' ||
      navigator.userAgent.indexOf('IEMobile') !== -1;
    return (
      <div>
        <h1>Imagenet</h1>
        <input
          type="file"
          name="image"
          accept="image/*"
          capture="camera"
          multiple
          onChange={this.handleSubmit}
        />
        {mobile ? <span /> : <CameraComponent handleImage={this.handleImg} />}
        <Grid gap="small" columns="medium" rows="medium">
          {this.renderImages()}
        </Grid>
      </div>
    );
  }
}

const stateToProps = state => state.imagenet;
const dispatchToProps = dispatch => ({
  getImagenet: img => dispatch(fetchImagenet(img)),
});

export default connect(
  stateToProps,
  dispatchToProps
)(Imagenet);
