import View from './View.js'

class UserView extends View {
    _parentElement = document.querySelector('.users');

    //template = `${email} ${username}`;

    addHandlerRender(handler) {
        window.addEventListener('load', handler);
    }
    _generateMarkup() {
        console.log(this._data);
        return this._data.map(result => `${result.email} ${result.username}<br>`).join('');
    }
}
export default new UserView();