import { resolve } from "path";
import { read } from "fs";

/**
 * 
 * @param {Blob} file
 * @return {Promise}
 */
export const getBase64Image = (file) => {
    return new Promise((resolve, reject) => {
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);;
        reader.onerror = (err) => reject(err);
    })
};
