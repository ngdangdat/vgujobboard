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
            initDate: {
                type: Date,
                default: null,
            },
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
            };
        },
        mounted() {
            if (this.initDate !== null) {
                this.date = this.initDate.getDate();
                this.month = this.initDate.getMonth();
                this.year = this.initDate.getFullYear();
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
                if (oldValue !== null && value == null) {
                    this.valid = false;
                } else {
                    this.validate();
                }
                this.$emit('change', value);
            },
        },
    });

export default DateSelectBox;

</script>

