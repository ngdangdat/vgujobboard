/**
 * @param {String} txt
 * @return {Boolean}
 */
export const isSnakeCase = (txt) => {
    if (txt.indexOf('_') !== -1) {
        return true;
    }
    return false;
};

/**
 * @param {String} src
 * @return {String}
 */
export const parseSnakeToCamel = (src) => {
    let parts = src.split('_');
    for (let idx = 0; idx < parts.length; idx++) {
        let part = parts[idx];
        if (idx == 0) {
            part = part.toLowerCase();
        } else if (idx > 0) {
            part = [].concat(
                part.slice(0, 1).toUpperCase(),
                part.slice(1, part.length).toLowerCase()
            ).join('');
        }
        parts[idx] = part;
    }
};
