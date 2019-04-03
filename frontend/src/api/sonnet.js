/***
 * Sonnet API
 */
import { buildAPIPath } from './config';

const makePath = buildAPIPath('sonnet');

const API = {
  generate: () => fetch(makePath('generate')).then(res => res.json()),
};

export default API;
