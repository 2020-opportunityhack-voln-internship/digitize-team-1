import axios from 'axios';

import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS
} from './types';

// REGISTER USER
export const register = ({ email, password, password2, first_name, last_name, npo }) => async dispatch => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body
  const body = JSON.stringify({ email, password, password2, first_name, last_name, npo });

  try {
    const res = await axios.post('http://127.0.0.1:8000/api/auth/register', body, config);
    dispatch({
      type: REGISTER_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: REGISTER_FAIL
    });
  }
};

// LOAD USER
export const loadUser = () => async (dispatch, getState) => {
    dispatch({type: USER_LOADING});

    try {
        const res = await axios.get('http://127.0.0.1:8000/api/auth/user', tokenConfig(getState));
        dispatch({
            type: USER_LOADED,
            payload: res.data
        });
    } catch (err) {
        dispatch({
            type: AUTH_ERROR
        });
    }
};

// LOGIN USER
export const login = ({ email, password }) => async dispatch => {
    // Headers
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    // Payload
    const body = JSON.stringify({ email, password });

    try {
        const res = await axios.post('http://127.0.0.1:8000/api/auth/login', body, config);
        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        });
    } catch (err) {
        dispatch({
            type: LOGIN_FAIL
        });
    }
};

// LOGOUT USER
export const logout = () => async (dispatch, getState) => {
    await axios.post('http://127.0.0.1:8000/api/auth/logout', null , tokenConfig(getState));
    dispatch({
        type: LOGOUT_SUCCESS
    })
}

// Helper function to get token
export const tokenConfig = getState => {
    // Get Token
    const token = getState().auth.token;

    // Headers
    const config = {
        headers: {
          'Content-Type': 'application/json'
        }
    };

    if (token) {
    config.headers['Authorization'] = `Token ${token}`;
    }

  return config;

};