import { parseSnakeToCamel, isSnakeCase, } from './string';

/**
 * 
 * @param {Object} object
 * @return {Object}
 */
export const switchSnakeToCamelObj = (srcObject) => {
    let resObject = new Object();
    for (let key in srcObject) {
        let value = srcObject[key];
        let keyToSet = key;
        if (isSnakeCase(key)) {
            keyToSet = parseSnakeToCamel(key);
        }
        resObject = Object.assign(resObject, {
            [keyToSet]: value,
        });
    }
    return resObject;
};
