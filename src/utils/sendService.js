import { postrequest, postrequest_body } from "./ajax";

// let preurl = "http://localhost:8080/";

let send_url = "https://1ba2de4f04.st1.iotda-app.cn-north-4.myhuaweicloud.com/v5/iot/b0a45b364a774797bb9945a2e1d38465/devices/6562fe1916c4bf776319996e_12345/commands";

let get_token_url = "https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens";

export const getTokenService = (data, callback) => {
    const url = get_token_url;
    let json = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "domain": {
                            "name": "haoru_pomelo" //IAM用户所属帐号名
                        },
                        "name": "member1", //IAM用户名
                        "password": "ZHR123456" //IAM用户密码
                    }
                }
            },
            "scope": {
                "project": {
                    "name": "cn-north-4" //IAM用户所属帐号名
                }
            }
        }
    }
    postrequest(url, json, callback);
}


export const sendService = (data, token, callback) => {
    const url = send_url;
    let send_data = {
        "service_id": "IOT",
        "command_name": "cmd1",
        "paras": {
            "button": data
        }
    }
    postrequest_body(url, send_data, token, callback);
}
