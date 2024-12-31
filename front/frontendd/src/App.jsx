import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import HomePages from './pages/homePrincipal.jsx';
import RegistrationPage from "./pages/regis.jsx";


const App = ()=> {
  return(
    <Router>
      <Routes>
      <Route path="/" element={<HomePages />} />
      <Route path="/register" element={<RegistrationPage />} />

      </Routes>
    </Router>
  );
};



export default App
