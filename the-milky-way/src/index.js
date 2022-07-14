import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./components/Home";
import Login from "./components/Login";
import Contact from "./components/Contact";
import NoPage from "./components/NoPage";
import './index.css'
import Forgot from "./components/Forgot";
import Register from "./components/Register";
import Flights from "./components/Flights";
import CustomerInput from "./components/CustomerInput";
export default function App() {
  
  return (
    <BrowserRouter>

      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home />} />
          <Route path="login" element={<Login/>} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
          <Route path="forgot-pwd" element={<Forgot />} />
          <Route path="register" element={<Register/>}/>
          <Route path="flights" element={<Flights/>}/>
          <Route path="customerInfo" element={<CustomerInput/>}/>
        </Route>

      </Routes>                

    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />)