import React from 'react';
import { Image as Img } from 'grommet';
import { parseImageSrc } from '../../utils/images';

class Image extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      src: '',
    };
  }

  componentDidMount() {
    parseImageSrc(this.props.src)
      .then(src => this.setState({ src }))
      .catch(console.log);
  }

  render() {
    return this.state.src === '' ? (
      <h1>Loading Image</h1>
    ) : (
      <Img fit={this.props.fit || 'cover'} src={this.state.src} />
    );
  }
}

export default Image;
