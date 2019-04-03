import React from 'react';
import { connect } from 'react-redux';
import { fetchSonnet } from '../store/actions/sonnet';
import API from '../api/imagenet';

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
    console.log(res);
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
    const img = this.uploadInput.files[0];
    API.predict(img).then(
      res => this.addImage(res, img),
      err => console.log(err)
    );
  }

  renderImages() {
    return this.state.images.map(img => (
      <ul key={img.data.name}>
        {img.predictions.map(p => (
          <li key={p.label}>
            {p.label} -- {p.probability}
          </li>
        ))}
      </ul>
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
            ref={ref => {
              this.uploadInput = ref;
            }}
          />
          <button>Predict</button>
        </form>
        <div>{this.renderImages()}</div>
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
