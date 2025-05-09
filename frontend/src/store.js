import { configureStore } from '@reduxjs/toolkit';
import userReducer from './features/userManagement/userSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
  },
});