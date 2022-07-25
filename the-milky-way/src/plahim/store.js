import {configureStore} from '@reduxjs/toolkit';
import userReducer from './userSlice';
import flightsReducer from './flightsSlice'
import customerReducer from './customerSlice'
export const store = configureStore({
    reducer:{
    user:userReducer,
    flights:flightsReducer,
    customer:customerReducer
}});
