import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./components/Home";
import Login from "./components/Login";
import Contact from "./components/Contact";
import NoPage from "./components/NoPage";
import Forgot from "./components/Forgot";
import Register from "./components/Register";
import Flights from "./components/Flights";
import CustomerInput from "./components/CustomerInput";
import TicketFinal from "./components/TicketFinal";
import MyTickets from "./components/MyTickets";
const App = ()=> {

    return (

        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Home />} />
              <Route path="login" element={<Login />} />
              <Route path="contact" element={<Contact />} />
              <Route path="*" element={<NoPage />} />
              <Route path="forgot-pwd" element={<Forgot />} />
              <Route path="register" element={<Register />} />
              <Route path="flights" element={<Flights />} />
              <Route path="customerInfo" element={<CustomerInput />} />
              <Route path="ticketFinal" element={<TicketFinal />} />
              <Route path="myTickets" element={<MyTickets></MyTickets>} />
            </Route>
          </Routes>
        </BrowserRouter>

    );
  };
export default App;  
