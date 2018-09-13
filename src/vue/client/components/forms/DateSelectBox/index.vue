<template>
    <div class="control three-cols">
        <div class="col select full-width">
            <select v-model="date">
                <option :value="null">{{ dateLabel }}</option>
                <option v-for="dateOption in dateList"
                    :key="dateOption.value"
                    :value="dateOption.value"
                >
                    {{ dateOption.display }}
                </option>
            </select>
        </div>
        <div class="col select full-width">
            <select v-model="month">
                <option :value="null">{{ monthLabel }}</option>
                <option v-for="monthOption in monthList"
                    :key="monthOption.value"
                    :value="monthOption.value"
                >
                    {{ monthOption.display }}
                </option>
            </select>
        </div>
        <div class="col select full-width">
            <select v-model="year">
                <option :value="null">{{ yearLabel }}</option>
                <option v-for="yearOption in yearList"
                    :key="yearOption.value"
                    :value="yearOption.value"
                >
                    {{ yearOption.display }}
                </option>
            </select>
        </div>
        <div v-if="errorMessage" class="error col full">
            <span>{{ errorMessage }}</span>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue';

    const monthDisplays = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ];

    let dates = new Array();
    for (let i = 1; i <= 31; i++) {
        dates.push({
            display: i.toString(),
            value: i,
        });
    }

    let months = new Array();
    for (let i = 0; i < 12; i++) {
        months.push({
            display: monthDisplays[i],
            value: i,
        });
    }

    let years = new Array();
    for (let i = 1979; i < 2001; i++) {
        years.push({
            display: i.toString(),
            value: i,
        });
    }

    const DateSelectBox = Vue.extend({
        props: {
            dateLabel: {
                type: String,
                default: 'Date',
            },
            monthLabel: {
                type: String,
                default: 'Month',
            },
            yearLabel: {
                type: String,
                default: 'Year',
            },
            value: {
                type: Date,
            },
            required: {
                type: Boolean,
            },
            requireMessage: {
                type: String,
                default: 'This field is required. Please choose a date.',
            },
            validationMessage: {
                type: String,
                default: 'Input date is invalid.',
            },
        },
        data() {
            return {
                date: null,
                month: null,
                year: null,
                dateList: dates,
                monthList: months,
                yearList: years,
                valid: true,
                errorMessage: '',
            };
        },
        mounted() {
            if (this.value !== null) {
                this.date = this.value.getDate();
                this.month = this.value.getMonth();
                this.year = this.value.getFullYear();
            }
        },
        methods: {
            validate() {
                const selectedDate = this.selectedDate;
                if (selectedDate === null) {
                    return;
                }

                if (selectedDate.getDate() == this.date &&
                    selectedDate.getMonth() == this.month &&
                    selectedDate.getFullYear() == this.year) {
                    this.valid = true;
                } else {
                    this.valid = false;
                    this.errorMessage = this.validationMessage;
                }
            },
        },
        computed: {
            selectedDate() {
                if (this.year && this.month && this.date) {
                    return new Date(this.year, this.month, this.date);
                }
                return null;
            },
        },
        watch: {
            selectedDate(value, oldValue) {
                let valueToSet = value;
                if (oldValue !== null && value === null) {
                    this.valid = false;
                } else {
                    this.validate();
                }
                if (!this.valid) {
                    valueToSet = null;
                }
                this.$emit('change', valueToSet);
            },
        },
    });

export default DateSelectBox;

</script>

