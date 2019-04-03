import React from 'react';
import { Grommet, Grid, Box } from 'grommet';
import Nav from '../components/Nav/Nav';

export default props => (
  <Grommet full theme={{ global: { colors: { doc: '#ff99cc' } } }}>
    <Nav />
    <Box pad="large" justify="center">
      {props.children}
    </Box>
  </Grommet>
);
