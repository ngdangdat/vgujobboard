
const LOGIN_REQUEST = 'LOGIN_REQUEST';
const LOGIN_REQUEST_PENDING = 'LOGIN_PENDING';
const LOGIN_REQUEST_SUCCESS = 'LOGIN_SUCCESS';
const LOGIN_REQUEST_FAILED = 'LOGIN_REQUEST_FAILED';

export const LOGIN_ACTIONS = {
    LOGIN_REQUEST,
    LOGIN_REQUEST_PENDING,
    LOGIN_REQUEST_SUCCESS,
    LOGIN_REQUEST_FAILED,
};

const PROFILE_REQUEST = 'PROFILE_REQUEST';
const PROFILE_REQUEST_SUCCESS = 'PROFILE_REQUEST_SUCCESS';
const PROFILE_REQUEST_PENDING = 'PROFILE_REQUEST_PENDING';
const PROFILE_REQUEST_FAILED = 'PROFILE_REQUEST_FAILED';

export const PROFILE_ACTIONS = {
    PROFILE_REQUEST,
    PROFILE_REQUEST_SUCCESS,
    PROFILE_REQUEST_PENDING,
    PROFILE_REQUEST_FAILED,
};

const REGISTER_REQUEST = 'REGISTER_REQUEST';
const REGISTER_REQUEST_SUCCESS = 'REGISTER_REQUEST_SUCCESS';
const REGISTER_REQUEST_PENDING = 'REGISTER_REQUEST_PENDING';
const REGISTER_REQUEST_FAILED = 'REGISTER_REQUEST_FAILED';
const REGISTER_REQUEST_RESET = 'REGISTER_REQUEST_RESET';

export const REGISTER_ACTIONS = {
    REGISTER_REQUEST,
    REGISTER_REQUEST_PENDING,
    REGISTER_REQUEST_SUCCESS,
    REGISTER_REQUEST_FAILED,
    REGISTER_REQUEST_RESET,
};

const MEMBER_DETAIL_REQUEST = 'MEMBER_DETAIL_REQUEST';
const MEMBER_DETAIL_REQUEST_SUCCESS = 'MEMBER_DETAIL_REQUEST_SUCCESS';
const MEMBER_DETAIL_REQUEST_PENDING = 'MEMBER_DETAIL_REQUEST_PENDING';
const MEMBER_DETAIL_REQUEST_FAILED = 'MEMBER_DETAIL_REQUEST_FAILED';

export const MEMBER_DETAIL_ACTIONS = {
    MEMBER_DETAIL_REQUEST,
    MEMBER_DETAIL_REQUEST_SUCCESS,
    MEMBER_DETAIL_REQUEST_PENDING,
    MEMBER_DETAIL_REQUEST_FAILED,
};

const MEMBER_LIST_REQUEST = 'MEMBER_LIST_REQUEST';
const MEMBER_LIST_REQUEST_CHANGE_PAGE = 'MEMBER_LIST_REQUEST_CHANGE_PAGE';
const MEMBER_LIST_REQUEST_SUCCESS = 'MEMBER_LIST_REQUEST_SUCCESS';
const MEMBER_LIST_REQUEST_PENDING = 'MEMBER_LIST_REQUEST_PENDING';
const MEMBER_LIST_REQUEST_FAILED = 'MEMBER_LIST_REQUEST_FAILED';

export const MEMBER_LIST_ACTIONS = {
    MEMBER_LIST_REQUEST,
    MEMBER_LIST_REQUEST_FAILED,
    MEMBER_LIST_REQUEST_PENDING,
    MEMBER_LIST_REQUEST_SUCCESS,
    MEMBER_LIST_REQUEST_CHANGE_PAGE,
};
