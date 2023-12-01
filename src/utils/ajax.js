export function postrequest(url, data, callback) {
    document.cookie = "name=ethereal;secure";
    let opts = {
        method: "POST",
        body: JSON.stringify(data),
        credentials: "include",
        headers: {
            'Content-Type': 'application/json',
        },
        mode: 'no-cors',
    }
    fetch(url, opts).then((response) => { 
        return response.headers.get('X-Subject-Token') })
        .then((data) => { callback(data) })
        .catch((error) => {
            console.log(error);
        })
        ;
}

export function postrequest_body(url, data, token, callback) {
    document.cookie = "name=ethereal;secure";
    let opts = {
        method: "POST",
        body: JSON.stringify(data),
        credentials: "include",
        headers: {
            'Content-Type': 'application/json',
            'X-Auth-Token': token,
        },
        mode: 'cors',
    }
    fetch(url, opts).then((response) => { 
        return response.json()})
        .then((data) => { callback(data) })
        .catch((error) => {
            console.log(error);
        })
        ;
}