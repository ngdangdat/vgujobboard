/**
 * Get headers
 * @returns {{Access-Control-Allow-Origin: string, X-Api-Version: string, X-Client: string}}
 */
export const getHeaders = () => {
  const headers = {};
  headers['Content-Type'] = 'application/json';
  if (window.localStorage && window.localStorage.getItem('token')) {
    headers.Authorization = `Token ${window.localStorage.getItem('token')}`;
  }
  return headers;
};
