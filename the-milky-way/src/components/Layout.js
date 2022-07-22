import { Outlet } from "react-router-dom";
const Layout = () => {
  const user = localStorage.getItem('user')
  
  
 
 return ( 
<>
<nav className="navbar navbar-expand bg-dark">
  <div className="container-fluid ">
    <a className="navbar-brand lg-dark" style={{color:'white'}} href="/">
    T M W
    </a>
    <div className="collapse navbar-collapse" id="navbarNav">
      <ul className="navbar-nav">
        <li className="nav-item ">
          <a className="btn btn-dark" aria-current="page" href="/">Home</a>
        </li>
        <li className="nav-item ">
          <a className="btn btn-dark" href="/contact">Contact</a>
        </li>
        <li className="nav-item ">
          <a className="btn btn-dark" href="/flights">Flights</a>
        </li>
        {user ? (
          <>
             <li className="nav-item">
             <a className="btn btn-dark" href="myTickets" style={{color:'green'}}>{JSON.parse(user).username}</a>
           </li>
           <li className="nav-item "> 
           <a className="btn btn-dark" href="/" style={{color:'red'}} onClick={()=>{
            localStorage.removeItem('user')
            localStorage.removeItem('token')
            localStorage.removeItem('tokenR')
            window.location.reload()
           }}>Logout</a>
         </li>
         </>
        ) : (
          <>
                <li className="nav-item">
                  <a className="btn btn-dark" href="login" style={{color:'red'}}>Login</a>
                </li>
                
                <li className="nav-item "> 
                  <a className="btn btn-link" href="register">Not Registerd?</a>
                </li>
                </>    
                )}
      </ul>
    </div>
  </div>
</nav>
<Outlet/>
</>
  )
};

export default Layout;
