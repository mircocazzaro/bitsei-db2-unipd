import { loadQueryOne } from './chart.js'

window.onpopstate = function (event) {
    switch (document.location.hash) {
        case '#query1':
            console.log('the home page was loaded')
            loadQueryOne()
            break;
        default:
            loadHome()
            break;
    }
};
