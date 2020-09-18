import { combineReducers } from 'redux';
import { LOGOUT_SUCCESS } from "../actions/types";
import auth from "./auth";

const appReducer = combineReducers({
  auth
});

//root reducer
const rootReducer = (state, action) => {
  if (action.type === LOGOUT_SUCCESS) {
    state = undefined;
  }
  return appReducer(state, action);
};

export default rootReducer;