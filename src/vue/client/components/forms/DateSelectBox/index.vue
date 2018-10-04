<template>
    <div class="control three-cols">
        <div class="col select full-width">
            <select class="input" :class="{'is-danger': error}" v-model="date">
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
            <select class="input" :class="{'is-danger': error}" v-model="month">
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
            <select class="input" :class="{'is-danger': error}" v-model="year">
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

    const isNullOrNaN = (val) => (!val || isNaN(val));

    /**
     * @param {Date} date
     * @param {Number} day
     * @param {Number} month
     * @param {Number} year
     * @return {Boolean}
     */
    const isDateValid = (date, day, month, year) => {
        if (!(date instanceof Date)) {
            console.log('ahoy');
            return false;
        }
        
        let isValid = true;

        if (date.getDate() !== day ||
            date.getMonth() !== month ||
            date.getFullYear() !== year) {
            console.log('ahoy 2');
            isValid = false;
        }

        return isValid;
    };

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

    const DateSelectBox = {
        $_veeValidate: {
            value() {
                return this.value;
            },
            name() {
                return this.name;
            }
        },
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
            name: {
                type: String,
            },
            error: {
                type: Boolean,
                default: false,
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
                }
            },
        },
        computed: {
            selectedDate() {
                let selectedDate;
                if (this.year && this.month && this.date) {
                    const date = new Date(this.year, this.month, this.date);
                    if (isDateValid(date, this.date, this.month, this.year)) {
                        selectedDate = date;
                    }
                }
                return selectedDate;
            },
        },
        watch: {
            selectedDate(value) {
                this.$emit('change', value);
            },
        },
    };

export default DateSelectBox;

</script>

