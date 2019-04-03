import React from 'react';
import { connect } from 'react-redux';
import { Grid } from 'grommet';
import { fetchSonnet } from '../store/actions/sonnet';
import API from '../api/imagenet';
import ImageCard from '../components/ImageCard/ImageCard';

class Imagenet extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      images: [],
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.addImage = this.addImage.bind(this);
  }

  addImage(res, img) {
    if (res.success) {
      const { predictions } = res;
      this.setState({
        images: [
          ...this.state.images,
          {
            data: img,
            predictions,
          },
        ],
      });
    }
  }

  handleSubmit(e) {
    e.preventDefault();
    const files = Array.from(this.uploadInput.files);
    files.map(img =>
      API.predict(img).then(
        res => this.addImage(res, img),
        err => console.log(err)
      )
    );
  }

  renderImages() {
    return this.state.images.map(img => (
      <ImageCard {...img} key={img.data.name + Math.random() + Date.now()} />
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

const stateToProps = state => state.sonnet;
const dispatchToProps = dispatch => ({
  getSonnet: () => dispatch(fetchSonnet()),
});

export default connect(
  stateToProps,
  dispatchToProps
)(Imagenet);
