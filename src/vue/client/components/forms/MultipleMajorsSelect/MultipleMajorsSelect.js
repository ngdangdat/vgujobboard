import Vue from 'vue';
import FontAwesomeIcon from '@/components/FontAwesomeIcon/index.vue';
import MajorSelect from '@/components/forms/MajorSelect/index.vue';

const MultipleMajorsSelectComponent = Vue.extend({
    components: {
        "major-select": MajorSelect,
        "icon": FontAwesomeIcon,
    },
    created() {
        this.handleListenedEvents();
    },
    props: {
        value: {
            type: null,
            required: false,
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
        selectWrapClass: {
            type: String,
            required: false,
        },
        majorMaxLength: {
            type: Number,
            required: false,
            default: 2,
        },
    },
    data() {
        return {
            majors: [{
                major: null,
                intake: null,
            }],
        };
    },
    computed: {
        isShowAddMoreBtn() {
            return this.majors.length < this.majorMaxLength;
        },
    },
    methods: {
        changeInputValue() {
            this.$emit('input', this.majors);
        },
        handleListenedEvents() {
            this.$on('changeMajorInput', (index, major, intake) => {
                this.majors[index] = Object.assign({}, this.majors[index], {
                    major,
                    intake,
                });
                this.changeInputValue();
                this.$forceUpdate();
            });
        },
        increaseMajorLength() {
            if (this.majors.length < this.majorMaxLength) {
                this.majors.push({
                    major: null,
                    intake: null,
                });
            }
        },
        getAllowedMajorsForCurrentInput(index) {
            let majorInputs = this.majors;
            let notAllowedIds = [];
            let allowedMajorList = this.majorList;
            for (let idx = 0; idx < majorInputs.length; idx++) {
                let majorInput = majorInputs[idx];
                if (idx !== index && majorInput.major !== null) {
                    notAllowedIds.push(majorInput.major.id);
                }
            }
            allowedMajorList = allowedMajorList.filter(major => (notAllowedIds.indexOf(major.id) == -1));
            return allowedMajorList;
        },
    },
    watch: {
        majors() {
            this.changeInputValue();
        },
    },
});

export default MultipleMajorsSelectComponent;
