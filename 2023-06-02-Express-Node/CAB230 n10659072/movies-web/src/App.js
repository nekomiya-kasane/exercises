import {
  Routes,
  Route,
  Navigate,
  useLocation,
  Link
} from "react-router-dom";
import Movies from './components/Movies'
import Home from './components/Home'
import RegisterPage from './components/Register'
import User from './components/User'
import LogoutPage from "./components/LogoutPage";
import React, { useEffect, useState } from 'react';
import MoviePage from  './components/MoviePage'
import { Menu } from 'antd';
import { HomeOutlined,VideoCameraOutlined,UserOutlined,LogoutOutlined,UserAddOutlined } from '@ant-design/icons';
import StarPage from "./components/StarPage";
import { refresh } from './api/userAPI';

function LandingPage() {
  const [selectedKeys,setSelectedKeys] = useState([])
  const location = useLocation();
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');

  useEffect(() => {
    const token = JSON.parse(localStorage.getItem('loginInfo'));
    if (token && token.bearerTokenexpirationTime > Date.now()) {
      setIsLoggedIn(true);
      setUsername(token.username);
    } else {
      setIsLoggedIn(false);
      setUsername('');
    }
  }, [location]);

  // Refresh token
  useEffect(() => {
    const refreshToken = async () => {
      const storedLoginInfo = JSON.parse(localStorage.getItem('loginInfo'));
      if (storedLoginInfo) {
        // Check if bearToken will expire before next  call
        if (Date.now()< storedLoginInfo.bearerTokenexpirationTime-10000) {
          // User is logged in and the access token has not expired yet
          setIsLoggedIn(true)
        } else if (Date.now() < storedLoginInfo.refreshTokenexpirationTime) {
          // Access token has expired but refresh token is still valid, so try to refresh the token
          try {
            const res = await refresh(storedLoginInfo.refreshToken.token)
            const bearerTokenexpirationTime = Date.now() + (res.bearerToken.expires_in*1e3);
            const refreshTokenexpirationTime = Date.now() + (res.refreshToken.expires_in*1e3);
            const loginInfo = {
              ...res.data,
              username:storedLoginInfo.username,
              bearerTokenexpirationTime,
              refreshTokenexpirationTime
            };
            localStorage.setItem(
              'loginInfo',
              JSON.stringify(loginInfo)
            );
          } catch (error) {
            // Refresh token failed, so user is logged out
            console.log(error)
            localStorage.removeItem('loginInfo');
            setIsLoggedIn(false);
          }
        } else {
          // Both access and refresh tokens have expired, so user is logged out
          localStorage.removeItem('loginInfo');
          setIsLoggedIn(false);
        }
      }
    };

    refreshToken();
    // Check login status every 10 seconds
    const intervalId = setInterval(refreshToken, 10000);
    return () => clearInterval(intervalId);
  }, []);

  const navigation = [
    { key: '/home', label: 'Home', icon: <HomeOutlined /> },
    { key: '/movies', label: 'Movies', icon: <VideoCameraOutlined /> },
    { key: '/register', label: 'Register', icon: <UserAddOutlined /> },
    { key: '/user', label: isLoggedIn ? username : 'Login', icon: <UserOutlined /> },
    { key: '/logout', label: 'logout', icon: <LogoutOutlined /> },
  ];

  useEffect(() => {
    const currentPath = location.pathname;
    setSelectedKeys([currentPath]);
  }, [location]);

  const handleMenuClick = (e) => {
    setSelectedKeys([e]);
  };

  useEffect(()=>{
    setSelectedKeys([window.location.pathname])
  },[])

  return (
    <div>
        <Menu
          theme="dark"
          mode="horizontal"
          style={{ height: '100%' }}
          selectedKeys={selectedKeys}
          onClick={handleMenuClick}
        >
          {navigation.map((item) => (
            <Menu.Item key={item.key} style={{ width: '20%' }}>
              <Link to={item.key}>
                <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-evenly' }}>
                  <div>{item.icon}</div>
                  <div>{item.label}</div>
                </div>
              </Link>
            </Menu.Item>
          ))}
        </Menu>
        <div>
          <Routes>
            <Route
              path="/"
              element={
                <Navigate to='/home' replace />
              }
            />
            <Route exact path={'/home'} element={<Home />} />
            <Route path={'/movies'} element={<Movies />} />
            <Route path={"/moviePage/:id"} element={<MoviePage />} />
            <Route path={'/register'} element={<RegisterPage/>}/>
            <Route path={'/user'} element={<User/>}/>
            <Route path={'/logout'} element={<LogoutPage/>}/>
            <Route path={'/people/:id'} element={<StarPage/>}/>
          </Routes>
        </div>
    </div>
  );
}

export default LandingPage;
