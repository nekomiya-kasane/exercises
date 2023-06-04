import React, { useState } from 'react';
import { Form, Input, Button, message,Typography } from 'antd';
import {useNavigate} from "react-router-dom";
import { register } from '../api/userAPI';
const RegisterPage = () => {
  const [form] = Form.useForm();
  const [loadings, setLoading] = useState(false);
  const navigate = useNavigate();
  const onFinish = async (values) => {
    try {
      setLoading(true);
        await register(values.username,values.password,);
      message.success('Registration successful');
      navigate('/user')
    } catch (error) {
      message.error('Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <Typography.Title>User Register</Typography.Title>
      <Form
        form={form}
        name="register"
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
          rules={[
            {
              type: 'email',
              message: 'The input is not a valid email',
            },
            {
              required: true,
              message: 'Please input your email',
            },
          ]}
        >
          <Input placeholder="Enter your email" />
        </Form.Item>
        <Form.Item
          name="password"
          label="Password"
          rules={[
            {
              required: true,
              message: 'Please input your password',
            },
          ]}
        >
          <Input.Password placeholder="Enter your password" />
        </Form.Item>
        <Form.Item
          name="confirmPassword"
          label="Confirm Password"
          dependencies={['password']}
          hasFeedback
          rules={[
            {
              required: true,
              message: 'Please confirm your password',
            },
            ({ getFieldValue }) => ({
              validator(_, value) {
                if (!value || getFieldValue('password') === value) {
                  return Promise.resolve();
                }
                return Promise.reject('The two passwords do not match');
              },
            }),
          ]}
        >
          <Input.Password placeholder="Confirm your password" />
        </Form.Item>
        <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
              <Button loading={loadings} type="primary" htmlType="submit">
                Register
              </Button>
            </Form.Item>
      </Form>
    </div>
  );
};

export default RegisterPage;
