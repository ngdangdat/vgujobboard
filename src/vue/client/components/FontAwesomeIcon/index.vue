<template>
    <i :class="`fas ${iconName} ${classes} ${iconSize}`"></i>
</template>

<script>
export default {
    name: 'FontAwesomeIcon',
    props: {
        name: {
            type: String,
            required: true,
        },
        classes: {
            type: String,
            required: false,
            default: '',
        },
        size: {
            type: String,
            required: false,
            default: '',
        }
    },
    computed: {
        iconName() {
            const name = this.name;
            return `fa-${name}`;
        },
        iconSize() {
            const size = this.size || '';
            if (!size) {
                return '';
            }
            return `fa-${size}`;
        },
    },
};
</script>

