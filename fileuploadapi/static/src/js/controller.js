import usersView from './views/usersView.js'
import sendPDFView from './views/sendPDFView.js'
import * as model from './model.js';

const controlUsers = async function () {

    const users = await model.loadUsers();
    usersView.render(users);
}
const controlAddPDF = async function (pdfFile) {
    console.log("★");
    console.log(pdfFile);
    const base64File = await fileToBase64(pdfFile);
    console.log(base64File);

    const a = await model.sendPDF(base64File);

}

const init = function () {
    // const text = "こんにちは世界!";

    // // エンコード
    // const encoded = btoa(text);
    // //=> "SGVsbG8sIHdvcmxkIQ=="
    // console.log(encoded);

    // const decoded = atob(encoded);

    usersView.addHandlerRender(controlUsers);
    sendPDFView.addHandlerSend(controlAddPDF);


};

const fileToBase64 = function (file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}

// var file = document.querySelector('#upload_pdffile').files[0];
// getBase64(file).then(
//     data => console.log(data)
// );

init();





