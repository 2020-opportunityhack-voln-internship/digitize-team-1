import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS
} from '../actions/types';

//initial state for whether a user is authenticated or not
const initialState = {
  isLoading: false,
  isAuthenticated: null,
  user: null,
  token: localStorage.getItem('token')
};

//reducer to update state of authentication based on action
export default function (state = initialState, action) {
    switch (action.type) {
        case USER_LOADING:
            return {
                ...state,
                isLoading: true
            };
        case USER_LOADED:
            return {
                ...state,
                isLoading: false,
                isAuthenticated: true,
                user: action.payload
            };
        case REGISTER_SUCCESS:
        case LOGIN_SUCCESS:
            localStorage.setItem('token', action.payload.token);
            return {
                ...state,
                isLoading: false,
                isAuthenticated: true,
                ...action.payload
            };
        case AUTH_ERROR:
        case REGISTER_FAIL:
        case LOGIN_FAIL:
            localStorage.removeItem('token');
            return {
                ...state,
                isLoading: false,
                isAuthenticated: false,
                user: null,
                token: null
            };
        case LOGOUT_SUCCESS:
            localStorage.removeItem('token');
            return {
                ...state,
                isLoading: false,
                isAuthenticated: false,
                user: null,
                token: null
            }
        default:
            return state;
    }
}