import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom';
import { selectCustomer, selectCustomerTickets, setCustomer, setCustomerTickets } from '../../plahim/customerSlice';
import { selectUser } from '../../plahim/userSlice'
import axios from 'axios';

const MyTickets = () => {
  const user = useSelector(selectUser);
  const customer = useSelector(selectCustomer);
  const customerTickets = useSelector(selectCustomerTickets);
  const dispatch = useDispatch();
  const nav = useNavigate();
  
  let token = localStorage.getItem('token')
  const config = {headers:{
    "Content-Type": "application/json",
    Authorization:"Bearer "+String(token)
  }}

  const getMyTickets= async()=>{
    if(customerTickets.length===0){
     axios.get(`http://127.0.0.1:8000/customer-tickets/${customer.id}`,config).then((response)=>{
        console.log('Response: ',response)
        dispatch(setCustomerTickets(response.data))
        console.log('customer tickets : ',customerTickets)
        })
    }
};    
getMyTickets();


  return (
    <div>
      MyTickets
      { customerTickets.map(( ticket, index ) => {
          return (
            <tr key={index}>
            <td>{ticket.name}</td>
            <td>{ticket.flight}</td>
          </tr>
            )})};
    </div>
  )
};

export default MyTickets;