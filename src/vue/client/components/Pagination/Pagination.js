import Vue from 'vue';

const Pagination = Vue.extend({
    props: {
        maxVisibleButtons: {
            type: Number,
            required: false,
            default: 3,
        },
        totalPages: {
            type: Number,
            required: true,
        },
        currentPage: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            page: null,
        };
    },
    mounted() {
        this.page = this.currentPage;
    },
    computed: {
        /**
         * @return {Boolean}
         */
        isQuickNavShow() {
            return this.totalPages > this.maxVisibleButtons;
        },
        startPage() {
            if (this.currentPage === 1) {
                return 1;
            }

            if (this.currentPage === this.totalPages && this.totalPages >= this.maxVisibleButtons) {
                return this.totalPages - this.maxVisibleButtons + 1;
            }

            return this.currentPage - 1;
        },
        pages() {
            let range = new Array();
            for (let i = this.startPage;
                i <= Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);
                i++
            ) {
                range.push({
                    num: i,
                    isDisabled: i === this.currentPage,
                });
            }

            return range;
        },
        firstPage() {
            return 1;
        },
        lastPage() {
            return this.totalPages;
        },
    },
    methods: {
        changePage(page) {
            this.$emit('changePage', page);
        },
        changePageWithInput(e) {
            const isValidInput = this.isPageInputValid(e.target.value);
            if (!isValidInput) {
                e.target.value = this.currentPage;
                return;
            }

            this.changePage(e.target.value);
        },
        isPageInputValid(pageInput) {
            if (isNaN(pageInput)) {
                return false;
            }

            const page = Number(pageInput);
            if (page >= 1 && page <= this.totalPages) {
                return true;
            }

            return false;
        },
    },
});

export default Pagination;
