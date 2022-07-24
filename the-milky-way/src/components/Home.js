import { React, useState } from "react";

const Home = () => {
   

    const [From, setFrom] = useState("")
    const [To, setTo] = useState("")
    const [depart, setDepart] = useState("")
    const [CLASS, setCLASS] = useState(1)
    const [adults, setAdults] = useState(1)
    const [flights, setFlights] = useState([]);
    const [table, setTable] = useState(0);
    
    const ShowFlights=async ()=>{
        if(table ===0){
          let request = await fetch("http://127.0.0.1:8000/getflights/");
          let response =await request.json();
          response.forEach(flight => {
            if(flight.from===From){
                if(flight.too===To){
                    flights.push(flight)
                }
            else if(flight.dep_date===depart){
                flights.push(flight)
            }
            else{alert("No flights for this parameters")}    
            }
          });

          setTable(1)
        }else{
          console.log('runing')
          return;
        }
      };

    return (
<div id="booking" className="section">
		<div className="section-center">
			<div className="container">
				<div className="row">
					<div className="booking-form">
        <form>
            <div className="form-group">
                <div className="form-checkbox">
                    <label htmlFor="roundtrip">
                        <input type="radio" id="roundtrip" name="flight-type"></input>
                        <span></span>Roundtrip
                    </label>
                    <label htmlFor="one-way">
                        <input type="radio" id="one-way" name="flight-type"></input>
                        <span></span>One way
                    </label>
                    
                </div>
            </div>
            <div className="row">
                <div className="col-md-6">
                    <div className="form-group">
                        <span className="form-label">Flying from</span>
                        <input className="form-control" type="text" placeholder="From >> Country" value={From} onChange={(e)=>setFrom(e.target.value)}></input>
                    </div>
                </div>
                <div className="col-md-6">
                    <div className="form-group">
                        <span className="form-label">Flyning to</span>
                        <input className="form-control" type="text" placeholder="To >>Country" value={To} onChange={(e)=>setTo(e.target.value)}></input>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col-md-3">
                    <div className="form-group">
                        <span className="form-label">Departing</span>
                        <input className="form-control" type="date" required value={depart} onChange={(e)=>setDepart(e.target.value)}></input>
                    </div>
                </div>
                <div className="col-md-3">
                    <div className="form-group">
                        <span className="form-label">Returning</span>
                        <input className="form-control" type="date" required></input>
                    </div>
                </div>
                <div className="col-md-2">
                    <div className="form-group">
                        <span className="form-label">Adults (18+)</span>
                        <select className="form-control" value={adults} onChange={(e)=>setAdults(e.target.value)}>
                            <option value={1}>1</option>
                            <option value={2}>2</option>
                            <option value={3}>3</option>
                        </select>
                        <span className="select-arrow"></span>
                    </div>
                </div>
                <div className="col-md-2">
                    <div className="form-group">
                        <span className="form-label">Children (0-17)</span>
                        <select className="form-control">
                            <option>0</option>
                            <option>1</option>
                            <option>2</option>
                        </select>
                        <span className="select-arrow"></span>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col-md-3">
                    <div className="form-group">
                        <span className="form-label">Travel className</span>
                        <select className="form-control" value={CLASS} onChange={(e)=>setCLASS(e.target.value)}>
                            <option value={1}>Economy class</option>
                            <option value={2}>Business class</option>
                            <option value={3}>First class</option>
                        </select>
                        <span className="select-arrow"></span>
                    </div>
                </div>
                <div className="col-md-3">
                    <div className="form-btn">
                        <button className="submit-btn" onClick={()=>ShowFlights()}>Show flights</button>
                    </div>
                </div>
            </div>
        </form>
					</div>
				</div>
			</div>
		</div>
	</div>

    );
  };
  
  export default Home;
  