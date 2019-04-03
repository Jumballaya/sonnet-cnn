import React from 'react';

const dataToString = imagedata => {
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = imagedata.width;
  canvas.height = imagedata.height;
  ctx.putImageData(imagedata, 0, 0);
  return canvas.toDataURL();
};

const fileToString = file =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = e => resolve(e.target.result);
    reader.readAsDataURL(file);
  });

const parseSrc = async src => {
  console.log(src, typeof src, src instanceof File);
  if (typeof src === 'string') return src;
  if (src instanceof ImageData) return dataToString(src);
  if (src instanceof File) return await fileToString(src);
  return '';
};

class Image extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      src: '',
    };
  }

  componentDidMount() {
    parseSrc(this.props.src)
      .then(src => this.setState({ src }))
      .catch(console.log);
  }

  render() {
    return this.state.src === '' ? (
      <h1>Loading Image</h1>
    ) : (
      <img src={this.state.src} />
    );
  }
}

export default Image;
