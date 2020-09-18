import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools-extension/index";
import reduxThunk from 'react-redux'
import rootReducer from './reducers'


//store used to store state
const store = createStore(
    rootReducer,
    composeWithDevTools(applyMiddleware(reduxThunk))
);