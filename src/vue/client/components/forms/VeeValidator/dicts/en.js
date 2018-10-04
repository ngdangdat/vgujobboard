
const emailValidationMsg = (fName) => `The ${fName.toLowerCase()} must be a valid email.`;
const confirmFieldMsg = (field, confirmField) => `The ${field.toLowerCase()} must match with ${confirmField}.`

export default {
    en: {
        messages: {
            email: emailValidationMsg,
            emailConfirm: emailValidationMsg,
            confirmed: confirmFieldMsg,
            required: (fN) => `Please input a valid ${fN}.`,
        },
        attributes: {
            emailConfirm: 'Email Confirmation',
            passwordConfirm: 'Password Confirmation'
        },
        custom: {

        },
    },
};