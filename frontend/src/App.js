import './App.css';
import ResponsiveAppBar from './components/Navigation'
import SignIn from './components/SignIn';
import HomePage from './components/Home';
import SignUp from './components/SignUp';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

function App() {
  return (
    <Router>
      <div className="App">
        <ResponsiveAppBar />

        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
          {/* Add more routes here */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
