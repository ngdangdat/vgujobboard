const notNullFilter = (val) => val !== null;

/**
 * Join strings into url
 * @param {String} paths
 * @returns {String}
 */
export const joinUrl = (...paths) => {
    return paths
        .filter(notNullFilter)
        .join('/')
        .replace(/(https?:\/\/)|(\/){2,}/g, "$1$2");
};
