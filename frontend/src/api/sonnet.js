/***
 * Sonnet API
 */
const apiURL = `${process.env.REACT_APP_API_BASE}`;
const baseURL = `${apiURL}/api/sonnet`;
const makePath = route => `${baseURL}${route}`;

const API = {
  generate: () => fetch(makePath(`/generate`)).then(res => res.json()),
};

export default API;
