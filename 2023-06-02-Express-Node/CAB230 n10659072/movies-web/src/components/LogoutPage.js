import React, { useEffect, useState } from 'react';
import { Button, Typography, message } from 'antd';
import {useNavigate} from "react-router-dom";
import { logout } from '../api/userAPI';
import  Trumen  from '../assets/Trumen.jpg'


const LogoutPage = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const navigate = useNavigate();
  const [loadings,setLoadings] = useState(false)
  useEffect(() => {
    const loginInfo = JSON.parse(localStorage.getItem('loginInfo'));
    if (loginInfo && loginInfo.bearerTokenexpirationTime > Date.now()) {
      setIsLoggedIn(true);
    }
  }, []);

  const styles = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: "90vh",
    backgroundImage: `url(${Trumen})`,
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center center',
    backgroundAttachment: 'fixed',
    backgroundSize: 'cover',
  };

  const handleLogout = async () => {
    try {
      setLoadings(true)
      const loginInfo = JSON.parse(localStorage.getItem('loginInfo'));
      const refreshToken = loginInfo.refreshToken.token;
      await logout(refreshToken)
      localStorage.removeItem('loginInfo');
      message.success('You have been logged out successfully!');
    } catch (error) {
        message.error(error);
    } finally{
      setLoadings(false)
      navigate('/user')
    }
  };

  return (
    <div style={styles}>
      {isLoggedIn ? (
        <div style={{ display: 'flex', flexDirection:'column', justifyContent: 'center', alignItems: 'center',position:'absolute',top:'50vh',right:'5vw'}}>
          <Typography.Title>Confirm to log out</Typography.Title>
          <Button type="primary" danger onClick={handleLogout} loading={loadings}>
            Logout
          </Button>
        </div>
      ) : (
        <Typography.Title style={{position:'absolute',top:'50vh',right:'5vw'}}>You are not logged in</Typography.Title>
      )}
    </div>
  );
};

export default LogoutPage;