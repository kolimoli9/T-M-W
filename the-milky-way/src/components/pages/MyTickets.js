import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom';
import { selectCustomer, selectCustomerTickets, setCustomerTickets } from '../../plahim/customerSlice';
import { selectUser } from '../../plahim/userSlice'
import axios from 'axios';

const MyTickets = () => {
  
  const user = useSelector(selectUser);
  const customer = useSelector(selectCustomer);
  const customerTickets = useSelector(selectCustomerTickets);
  const dispatch = useDispatch();
  const nav = useNavigate();
  
  let url = 'http://127.0.0.1:8000/customer-tickets/'
  let token = localStorage.getItem('token')
  let config = {headers:{
    "Content-Type": "application/json",
    Authorization:"Bearer "+String(token)
  }}

  window.onload= async()=>{
    if(customerTickets.length===0){
     axios.get(url+customer.id,config).then((response)=>{
        console.log('Response: ',response)
        dispatch(setCustomerTickets(response.data))
        console.log('customer tickets : ',customerTickets)
        })
    }
};    



  return (
    <div>
      MyTickets

    </div>
  )
};

export default MyTickets;