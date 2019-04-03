import React from 'react';
import { Link } from 'react-router-dom';
import { Anchor, Heading, Box, Text } from 'grommet';

const linkStyle = {
  color: '#7D4CDB',
};

const Nav = props => (
  <Box
    background="light-2"
    direction="column"
    pad="small"
    justify="center"
    align="center"
  >
    <Box pad="small">
      <Text size="xxlarge">Machine Learning Tools</Text>
    </Box>
    <Box justify="center" align="center" pad="small">
      <Text level={4}>
        <Anchor href="#">
          <Link to="/" style={linkStyle}>
            Back Home
          </Link>
        </Anchor>
      </Text>
      <Text level={4}>
        <Anchor href="#">
          <Link to="/sonnet" style={linkStyle}>
            Sonnet Generator
          </Link>
        </Anchor>
      </Text>
      <Text level={4}>
        <Anchor href="#">
          <Link to="/imagenet" style={linkStyle}>
            Imagenet
          </Link>
        </Anchor>
      </Text>
    </Box>
  </Box>
);

export default Nav;
