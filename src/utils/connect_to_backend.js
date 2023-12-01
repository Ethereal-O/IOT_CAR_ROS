import * as Sendservice from './sendService';

export function getTokenService(data, callback) {
    let senddata = new FormData();
    Sendservice.getTokenService(senddata, callback);
}

export function sendConnect(data, token, sendcallback) {
    Sendservice.sendService(data, token, sendcallback);
}
