import { API_URL } from "./config.js";
import { getJson, sendJson } from "./helper.js";

export const status = {

}
export const loadUsers = async function (id) {
    // const url = 'http://localhost:8000/aapi/users';
    // const request = new XMLHttpRequest();
    // request.open('GET', 'http://localhost:8000/api/users');
    // request.send();
    // request.onload = () => {
    //     const text = request.responseText;
    //     console.log(text);
    //     const json = JSON.parse(text);
    //     return json;
    // }
    // return fetch(url)
    //     .then(response => {
    //         if (!response.ok) throw new Error(`${response.status} ${response.statusText}`)
    //         return response.json();
    //     })
    //     .catch(err => {
    //         console.error(err);
    //     });
    try {
        // const res = await fetch(url);
        // if (!res.ok) throw new Error(`${response.status} ${response.statusText}`);
        // return res.json();

        const data = await getJson(`${API_URL}api/users/`);
        return data;
    } catch (err) {
        console.error(err);
    }
}

export const sendPDF = async function (data) {
    try {
        // TODO formから
        const sendData = {
            system_code: 1,
            file_id: 2,
            pdf_file: data,
            status_cd: 4,
        };
        await sendJson(`${API_URL}api2/tsreq/`, sendData);
    } catch (err) {
        console.error(err);
    }
}
