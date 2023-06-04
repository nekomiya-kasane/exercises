import React, { useState, useEffect } from 'react';
import { Input, Button, Form, Typography, message } from 'antd';
import { login } from '../api/userAPI';
import {useNavigate} from "react-router-dom";

function User() {
  const [loadings, setLoadings] = useState(false);
  const [error, setError] = useState('');
  const [loginInfo, setLoginInfo] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    // check if there is login information stored in local storage
    const storedLoginInfo = localStorage.getItem('loginInfo');
    if (storedLoginInfo) {
      const parsedLoginInfo = JSON.parse(storedLoginInfo);
      const expirationTime = parsedLoginInfo.bearerTokenexpirationTime;
      // check if the login information is not expired
      if (expirationTime && expirationTime > Date.now()) {
        setLoginInfo(parsedLoginInfo);
      } else {
        // clear the expired login information from local storage
        localStorage.removeItem('loginInfo');
      }
    }
  }, []);

  const onFinish = async (values) => {
    setLoadings(true);
    try {
      const res = await login(values.username, values.password);
      // set the login information to local storage
      const bearerTokenexpirationTime = Date.now() + (res.data.bearerToken.expires_in*1e3);
      const refreshTokenexpirationTime = Date.now() + (res.data.refreshToken.expires_in*1e3);
      const loginInfo = {
        ...res.data,
        username:values.username,
        bearerTokenexpirationTime,
        refreshTokenexpirationTime
      };
      const loginInfoString = JSON.stringify(loginInfo);
      localStorage.setItem('loginInfo', loginInfoString);
      setLoginInfo(loginInfo);
      message.success('Login successful');
      setLoadings(false);
      navigate('/home')
    } catch {
      setError('error');
      setLoadings(false)
      message.error('Incorrect Username/Password ! ');
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      {loginInfo ? (
        <Typography.Title>Welcome {loginInfo.username}!</Typography.Title>
      ) : (
        <>
          <Typography.Title>User Login</Typography.Title>
          <Form
            name="login"
            labelCol={{ span: 8 }}
            wrapperCol={{ span: 16 }}
            style={{ maxWidth: 600, padding: '10px' }}
            initialValues={{ remember: true }}
            onFinish={onFinish}
            autoComplete="off"
          >
            <Form.Item
              label="Username"
              name="username"
              rules={[{ required: true, message: 'Please input your username!' }]}
            >
              <Input status={error} />
            </Form.Item>

            <Form.Item
              label="Password"
              name="password"
              rules={[{ required: true, message: 'Please input your password!' }]}
            >
              <Input.Password status={error} />
            </Form.Item>
            <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
              <Button loading={loadings} type="primary" htmlType="submit">
                LogIn
              </Button>
            </Form.Item>
          </Form>
        </>
      )}
      <Typography>All data is from IMDB, Metacritic and RottenTomatoes. © 2023 Yuxuan Wang</Typography>
    </div>
  );
}

export default User;
