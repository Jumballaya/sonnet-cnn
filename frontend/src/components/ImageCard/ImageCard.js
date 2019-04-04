import React from 'react';
import { Box, Meter, Text } from 'grommet';
import Image from '../Image/Image';

const Probility = props => (
  <Box direction="row" align="center" justify="between" pad="xsmall">
    <Box direction="column" align="start">
      <Text>{props.label}</Text>
      <Meter
        type="bar"
        background="white"
        size="small"
        thickness="small"
        values={[{ value: props.probability * 100 }]}
      />
    </Box>
    <Text>{Math.round(props.probability * 100)}%</Text>
  </Box>
);

const ImageCard = props => (
  <Box animation="fadeIn" pad="small" background="light-1">
    <Image src={props.data} />
    <Box pad="small">
      {props.predictions.map(p => (
        <Box key={p.label + (props.data.name || Math.random())}>
          <Probility {...p} />
        </Box>
      ))}
    </Box>
  </Box>
);

export default ImageCard;
