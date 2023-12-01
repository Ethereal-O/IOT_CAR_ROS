import React from 'react';
import { withRouter } from "react-router-dom";
import { Button } from 'antd';
import { Form, Input, Checkbox } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import '../css/sender.css';
import { sendConnect, getTokenService } from '../utils/connect_to_backend';

// import * from './utils/connect_to_backend';

class Sender extends React.Component {

    gettokencallback = (data) => {
        this.state.token = data;
    }

    constructor(){
        super();
        getTokenService({}, this.gettokencallback);
        this.state = {
            token : ""
        }
    }

    render() {
        let callback = (data) => {
            console.log(data);
        }

        let send = (data) => {
            sendConnect(data, this.state.token, (data) => {callback(data)});
        }

        return (
            <div className="login-page">
                <div className="login-container">
                    <div className="login-box">
                        <h1 className="page-title">智能车控系统</h1>
                        <div className="login-content">
                            <Form
                                name="normal_login"
                                className="login-form"
                                initialValues={{
                                    remember: true,
                                }}
                                size={"large"}
                            >
                                <Form.Item>
                                    <Button type="primary" htmlType="submit" className="login-form-button" onClick={()=>{send('0')}}>
                                        加速
                                    </Button>
                                </Form.Item>
                                <Form.Item>
                                    <Button type="primary" htmlType="submit" className="login-form-button" onClick={()=>{send('1')}}>
                                        减速
                                    </Button>
                                </Form.Item>
                                <Form.Item>
                                    <Button type="primary" htmlType="submit" className="login-form-button" onClick={()=>{send('2')}}>
                                        左转
                                    </Button>
                                </Form.Item>
                                <Form.Item>
                                    <Button type="primary" htmlType="submit" className="login-form-button" onClick={()=>{send('3')}}>
                                        右转
                                    </Button>
                                </Form.Item>
                            </Form>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default withRouter(Sender);