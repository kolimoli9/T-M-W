import { createSlice } from "@reduxjs/toolkit";
const initialState = {
    value: [],
    flight: null,
};
export const flightsSlice = createSlice({
    name: 'flights',
    initialState,
    reducers:{
        setFlights: (state,action)=>{
            state.value = action.payload
        },
        setChosenFlight: (state,action)=>{
            state.flight = action.payload
        },
    }
});

export const {setFlights, setChosenFlight} = flightsSlice.actions;
export const selectFlights = (state)=>state.flights.value;
export const selectChosenFlight = (state)=>state.flights.flight;
export default flightsSlice.reducer;