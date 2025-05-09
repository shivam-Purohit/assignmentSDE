import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    isLoggedIn: false,
  };
  
  const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
      markLogged: (state) => {
        state.isLoggedIn = true;
      },
      markNotLogged: (state) => {
        state.isLoggedIn = false;
      },
    },
  });
  
  export const { markLogged, markNotLogged } = userSlice.actions;
  export default userSlice.reducer;