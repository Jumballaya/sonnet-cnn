import React from 'react';
import { connect } from 'react-redux';
import { Grid } from 'grommet';
import { fetchImagenet } from '../store/actions/imagenet';
import API from '../api/imagenet';
import ImageCard from '../components/ImageCard/ImageCard';
import { Camera } from '../utils/images';

class Imagenet extends React.Component {
  constructor(props) {
    super(props);

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleTakePic = this.handleTakePic.bind(this);
  }

  handleSubmit(e) {
    e.preventDefault();
    const files = Array.from(this.uploadInput.files);
    files.map(img => this.props.getImagenet(img));
  }

  handleTakePic(e) {
    e.preventDefault();
    const c = new Camera(640, 480);
    c.capture().then(img => this.props.getImagenet(img));
  }

  renderImages() {
    const key = name => (name || 'image-card') + Math.random() + Date.now();
    return this.props.images.map(img => (
      <ImageCard {...img} key={key(img.data.name)} />
    ));
  }

  render() {
    return (
      <div>
        <h1>Imagenet</h1>
        <form onSubmit={this.handleSubmit}>
          <input
            type="file"
            name="image"
            accept="image/png, image/jpg, image/jpeg"
            multiple
            ref={ref => {
              this.uploadInput = ref;
            }}
          />
          <button>Predict</button>
        </form>
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
