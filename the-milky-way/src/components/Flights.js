import React, {  useState } from 'react';
const Flights = () => {
  

    const [flights, setFlights] = useState([]);
    const [table, setTable] = useState(0);
    
    const getFlights=async ()=>{
      if(table ===0){
        let request = await fetch("http://127.0.0.1:8000/getflights/");
        let response =await request.json();
        setFlights(response);
        setTable(1)
      }else{
        return;
      }
    };
    getFlights();
   
    const orderNow = async (flight)=>{
      const user = localStorage.getItem('user')
      if(user===null){
        alert('You Need To Sign In First !')
        window.location.href = "/login"
      // window.location.href = "/customerInfo";
    }else{     
      localStorage.setItem('flight',JSON.stringify(flight))
      window.location.href="/customerInfo"
    };
  };
    
  return (
    <div className='flights'>
      
    <div className='container'>

<table className="table table-dark table-striped">

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
{flights.map(( flight, index ) => {
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
              <td><button className='btn btn-success' onClick={()=>orderNow(flight)}>Order Now!</button></td>
            </tr>
          );
        })}
</tbody>
    </table>
    </div>  
   
    </div>
  )
}

export default Flights