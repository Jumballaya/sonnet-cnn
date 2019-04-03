import React from 'react';
import { connect } from 'react-redux';
import { fetchSonnet } from '../store/actions/sonnet';

class Sonnet extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.props.getSonnet();
  }

  render() {
    return (
      <div>
        <h1>Sonnet</h1>
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
)(Sonnet);
