/**
 * Get headers
 * @returns {{Access-Control-Allow-Origin: string, X-Api-Version: string, X-Client: string}}
 */
export const getHeaders = () => {
    const headers = {
      'Access-Control-Allow-Origin': '*',
    };

    // if (window.localStorage && window.localStorage.getItem('token')) {
    //   headers.Authorization = `Bearer ${window.localStorage.getItem('token')}`;
    // }
    return headers;
  };
