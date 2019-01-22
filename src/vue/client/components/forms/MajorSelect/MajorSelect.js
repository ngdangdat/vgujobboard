import Vue from 'vue';
import FontAwesomeIcon from '@/components/FontAwesomeIcon/index.vue';

const getCurrentYear = () => (new Date()).getFullYear();

const MajorSelectComponent = Vue.extend({
    components: {
        "icon": FontAwesomeIcon,
    },
    props: {
        id: {
            type: Number,
            required: true,
        },
        majorList: {
            type: Array,
            required: true,
        },
        wrapClass: {
            type: String,
            required: false,
        },
        inputClass: {
            type: String,
            required: false,
        },
    },
    data() {
        return {
            majorId: null,
            major: null,
            intake: null,
            acceptedYears: [],
            validMajorInput: false,
        };
    },
    methods: {
        changeMajor() {
            let acceptedYears = new Array();
            this.intake = null;
            if (this.major !== null) {
                const fromYear = this.major.start_from;
                const currentYear = getCurrentYear();
                for (let i = fromYear; i < currentYear; i++) {
                    acceptedYears.push(i);
                }
            }
            this.acceptedYears = acceptedYears;
            this.change();
        },
        change() {
            const index = this.id;
            this.$parent.$emit('changeMajorInput', index, this.major, this.intake);
        },
        getMajorFromId(id) {
            return this.majorList.filter(major => major.id === id)[0];
        }
    },
    watch: {
        majorId(id) {
            this.major = this.getMajorFromId(id);
            this.changeMajor();
        }
    },
});

export default MajorSelectComponent;
