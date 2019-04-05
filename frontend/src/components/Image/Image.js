import React from 'react';
import { Image as Img } from 'grommet';
import Loader from 'react-loaders';
import { parseImageSrc } from '../../utils/images';
import './image.css';

const which = (comp1, comp2) => check => (check ? comp1 : comp2);

const ImageNormal = props => {
  const { src, fit, toggle } = props;
  return (
    <Img className="small" fit={fit || 'cover'} src={src} onClick={toggle} />
  );
};

const ImageFullscreen = props => {
  const { src, fit, toggle } = props;
  return (
    <Img
      className="fullscreen-image"
      fit={fit || 'contain'}
      src={src}
      onClick={toggle}
    />
  );
};

class Image extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      src: '',
      fullscreen: false,
    };
    this.toggleFullscreen = this.toggleFullscreen.bind(this);
  }

  componentDidMount() {
    parseImageSrc(this.props.src)
      .then(src => this.setState({ src }))
      .catch(console.log);
  }

  toggleFullscreen() {
    this.setState({
      fullscreen: !this.state.fullscreen,
    });
  }

  render() {
    const { src, fullscreen } = this.state;
    const fit = this.props.fit || 'cover';

    const loader = (
      <div className="loader">
        <Loader type="line-scale-party" size="large" />
      </div>
    );
    const normal = (
      <ImageNormal fit={fit} src={src} toggle={this.toggleFullscreen} />
    );
    const fs = (
      <div className="fullscreen-container">
        <ImageFullscreen fit={fit} src={src} toggle={this.toggleFullscreen} />
      </div>
    );

    const image = which(fs, normal)(fullscreen);
    return which(loader, image)(src === '');
  }
}

export default Image;
