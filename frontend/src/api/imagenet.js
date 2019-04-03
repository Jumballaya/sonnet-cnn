/***
 * Sonnet API
 */
import { buildAPIPath } from './config';

const makePath = buildAPIPath('imagenet');

const postImage = img => {
  const image = new FormData();
  image.append('image', img);

  return {
    method: 'POST',
    body: image,
  };
};

const API = {
  predict: img =>
    fetch(makePath('predict'), postImage(img)).then(res => res.json()),
};

export default API;
