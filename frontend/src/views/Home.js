import React from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';

const Home = props => (
  <div>
    <h1>Home route!</h1>
    <Link to="/sonnet">Sonnet Page</Link>
  </div>
);

export default connect()(Home);
