/***
 * Sonnet API
 */
const apiURL = 'http://localhost:5000';
const baseURL = `${apiURL}/api/sonnet`;
const makePath = route => `${baseURL}${route}`;

const API = {
  generate: () => fetch(makePath(`/generate`)).then(res => res.json()),
};

export default API;
