import View from './View.js';

class SendPDFView extends View {
    _parentElement = document.querySelector('#file_upl_btn');
    _message = 'PDF was successfully send :)';

    constructor() {
        super();
    }


    addHandlerSend(handler) {
        this._parentElement.addEventListener('click', function () {
            const pdfFile = document.querySelector('#upload_pdffile').files[0];

            handler(PDFFile);
        });
    }

    _generateMarkup() { }
}

export default new SendPDFView();
