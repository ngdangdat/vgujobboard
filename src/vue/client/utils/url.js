const notNullFilter = (val) => val !== null;

export default {
    /**
     * Join strings into url
     * @param {String} paths
     * @returns {String}
     */
    joinUrl: (...paths) => {
        return paths
            .filter(notNullFilter)
            .join('/')
            .replace(/\/+/g, '/');
    },
};
