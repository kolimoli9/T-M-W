import { createSlice } from "@reduxjs/toolkit";
const initialState = {
    value: null,
};
export const customerSlice = createSlice({
    name: 'customer',
    initialState,
    reducers:{
        setcustomer: (state,action)=>{
            state.value = action.payload
        },
        
    }
});

export const {setCustomer} = customerSlice.actions;
export const selectCustomer = (state)=>state.customer.value;
export default customerSlice.reducer;