import React from 'react';
import { Box } from 'grommet';
import Image from '../Image/Image';

const ImageCard = props => (
  <Box pad="small">
    <Image src={props.data} />
    <ul key={props.data.name}>
      {props.predictions.map(p => (
        <li key={p.label}>
          {p.label} -- {p.probability}
        </li>
      ))}
    </ul>
  </Box>
);

export default ImageCard;
