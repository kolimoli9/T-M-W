import React, { useEffect, useState } from 'react'
import {  useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { selectUser } from '../../../plahim/userSlice';
import { selectFlights, setFlights } from '../../../plahim/flightsSlice';
import axios from 'axios';

const Airline = () => {
  const dispatch=useDispatch()
  const user = useSelector(selectUser);
  const nav=useNavigate()
  const [AirlineFlights, setAirlineFlights] = useState([])
  const flights = useSelector(selectFlights)
  const token = localStorage.getItem('token')
  const config={headers:{
    "Content-Type": "application/json",
    Authorization:"Bearer "+String(token)
  }}

  const refreshFlights= async ()=>{
      let request = await fetch("https://my-server-for-tmw.herokuapp.com/getflights/");
      let response = await request.json();
      dispatch(setFlights((response)));
  };

  const deleteFlight =async (flight)=>{
     axios.delete(`http://127.0.0.1:8000/flights/${flight.id}`,config).then((response)=>{alert(JSON.stringify(response.data))});
     refreshFlights();
  };
  
  const updateFlight=async(flight)=>{
    console.log('Update flight num:',flight.id)
 
  };



  useEffect(()=>{
    if(AirlineFlights.length===0){
    const tempFlights = []
    flights.forEach(flight => {
      if(flight.airline===user.airline){
        tempFlights.push(flight)
      }
    });
    setAirlineFlights(tempFlights);
  }else{
    console.log('useEffect Run')
  }
  }) 
  
  return (
    <div className='shadow-lg p-3 mb-5 bg-body rounded'>
        
<table className="table table-dark table-striped" >
    <thead style={{'backgroundColor':'black'}}>
    <tr >
    <th>ID</th>
    <th>TICKETS</th>
    <th>FROM..</th>
    <th>TO..</th>
    <th>AIRLINE</th>
    <th>DEPARTURE</th>
    <th>Take Of</th>
    <th>ARRIVAL</th>
    <th>Land</th>
    </tr>
    </thead>
<tbody>
  
{ AirlineFlights.map(( flight, index ) => {
          return (
            <tr key={index}>
              <td>{flight.id}</td>
              <td>{flight.tickets}</td>
              <td>{flight.from}</td>
              <td>{flight.too}</td>
              <td>{flight.airline}</td>
              <td>{flight.dep_date}</td>
              <td>{flight.dep_time}</td>
              <td>{flight.arrival_date}</td>
              <td>{flight.arrival_time}</td> 
              <td><button className='btn btn-danger' onClick={()=>deleteFlight(flight)}>Delete</button></td>
              <td><button className='btn btn-info' >Update</button></td>
            </tr>
          );
        })}
        <tr>
        <td><button className='btn btn-success'>Add</button></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        </tr>
    </tbody>
</table>
        </div>
  )
}

export default Airline