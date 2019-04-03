/**
 * API tools
 */

const BASE_URL = `${process.env.REACT_APP_API_BASE}`;

export const buildAPIPath = feature => route =>
  `${BASE_URL}/api/${feature}/${route}`;
