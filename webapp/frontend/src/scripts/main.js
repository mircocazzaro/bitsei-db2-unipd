import Chart from "chart.js/auto";
import {loadQueryOne} from './chart.js'

let chart;

const loading = document.createElement('div');
loading.classList.add('col');
loading.innerHTML = '<div class="spinner-border" role="status">' +
    '<span class="sr-only">Loading...</span>' +
    '</div>';

window.onpopstate = function (event) {
    // add loading for each page here inside the row div of main tag of the index.html
    const main = document.querySelector('main');
    const rowDiv = main.getElementsByClassName('row')

    // append loading to the row div
    rowDiv[0].appendChild(loading);

    // get the h1 and p tag of the main tag
    const h1Title = main.getElementsByTagName('h1');
    const mainDescription = main.getElementsByTagName('p');

    // remove the chart if it exists, and it's instance of Chart.js
    if (chart || chart instanceof Chart) {
        chart.destroy();
    }

    switch (document.location.hash) {
        case '':
        case '#':
            rowDiv[0].removeChild(loading);
            break;
        case '#query1':
            h1Title[0].innerHTML = 'Query 1';
            mainDescription[0].innerHTML = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod, nisl sed lacinia ultrices, nunc nunc aliquam nunc, nec aliquam nunc nu';

            loadQueryOne(loading).then(r => {
                rowDiv[0].removeChild(loading)
                chart = new Chart(
                    document.getElementById('chart'),
                    r
                );
            });

            break;
        case '#query2':
            h1Title[0].innerHTML = 'Query 2';
            mainDescription[0].innerHTML = 'Lorem others';

            loadQueryOne(loading).then(r => {
                rowDiv[0].removeChild(loading)
                chart = new Chart(
                    document.getElementById('chart'),
                    r
                );
            });

            break;
        default:
            loadQueryOne(loading).then(r => rowDiv[0].removeChild(loading));
            break;
    }
};
