import {React } from 'react'
import { Link, Outlet } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';
import { selectUser, setTheUser} from '../../plahim/userSlice'
const Layout=()=> { 
  const dispatch = useDispatch()
  const user = useSelector(selectUser)
  window.onload=()=>{
    let savedUser = localStorage.getItem('user')
    console.log('savedUser: ',savedUser)
    if(savedUser!=null){
        let signedIn = JSON.parse(savedUser)
        dispatch(setTheUser(signedIn))
    }
  };
  console.log(user)
  return (
    <>
      <nav className="navbar navbar-expand bg-dark">
        <div className="container-fluid ">
          <a className="navbar-brand lg-dark" style={{ color: 'white' }} href="/">
            T M W
          </a>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
          
              <li className="nav-item ">
                <Link className="btn btn-dark" aria-current="page" to="/">Home</Link>
              </li>
              <li className="nav-item ">
                <Link className="btn btn-dark" to="contact">Contact</Link>
              </li>
              <li className="nav-item ">
                <Link className="btn btn-dark" to="flights">Flights</Link>
              </li>
              {user ? (
                <>
                  <li className="nav-item">
                    <Link className="btn btn-dark" to="myTickets" style={{ color: 'green' }}>{user.email}</Link>
                  </li>
                  <li className="nav-item ">
                    <Link className="btn btn-dark" to="/" style={{ color: 'red' }} onClick={() => {
                      localStorage.removeItem('token');
                      localStorage.removeItem('tokenR');
                      localStorage.removeItem('user')
                      window.location.href='/';
                    } }>Logout</Link>
                  </li>
                </>
              ) : (
                <>
                  <li className="nav-item">
                    <Link className="btn btn-dark" to="login" style={{ color: 'red' }}>Login</Link>
                  </li>

                  <li className="nav-item ">
                    <Link className="btn btn-link " to="register">Not Registerd?</Link>
                  </li>
                </>
              )}
              
            </ul>
          </div>
        </div>
      </nav>
      <Outlet />
    </>
  );
}

export default Layout;
