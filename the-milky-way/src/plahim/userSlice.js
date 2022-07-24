import { createSlice } from "@reduxjs/toolkit";
const initialState = {
    value: false,
};
export const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers:{
        setTheUser: (state,action)=>{
            state.value = action.payload
            console.log("the user", action.payload)
        },test:(state)=>{
         console.log(  state.value)
        },
    }
});

export const {setTheUser,test} = userSlice.actions;
export const selectUser = (state)=>state.user.value;
export default userSlice.reducer;