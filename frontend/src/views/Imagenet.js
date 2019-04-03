import React from 'react';
import { connect } from 'react-redux';
import { fetchSonnet } from '../store/actions/sonnet';

class Imagenet extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.props.getSonnet();
  }

  render() {
    return (
      <div>
        <h1>Imagenet</h1>
        <p>{this.props.sonnet.sonnet}</p>
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
