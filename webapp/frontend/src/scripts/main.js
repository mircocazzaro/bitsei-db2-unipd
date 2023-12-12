import Chart from "chart.js/auto";
import {ChoroplethController, GeoFeature, ColorScale, ProjectionScale} from 'chartjs-chart-geo';

import {loadQueryOne, loadQueryTwo, loadQueryThree, loadMap} from './chart.js'

let chart;

const loading = document.createElement('div');
loading.classList.add('col');
loading.innerHTML = '<div class="spinner-border" role="status">' +
    '<span class="sr-only">Loading...</span>' +
    '</div>';


function addSelectElement(selectElement, mainDescription, options, func) {
    const {parentNode} = mainDescription;
    for (let i = 0; i < parentNode.childNodes.length; i++) {
        if (parentNode.childNodes[i].nodeName === 'SELECT') {
            parentNode.removeChild(parentNode.childNodes[i]);
            break;
        }
    }
    
    for (let option of options) {
        let optionElement = document.createElement("option");
        optionElement.value = option.value;
        optionElement.text = option.text;
        selectElement.appendChild(optionElement);
    }
    
    selectElement.onchange = func;

    parentNode.insertBefore(selectElement, mainDescription);
}

window.onpopstate = function (event) {
    // add loading for each page here inside the row div of main tag of the index.html
    const main = document.querySelector('main');
    const rowDiv = main.getElementsByClassName('row')

    // append loading to the row div
    rowDiv[0].appendChild(loading);

    // get the h1 and p tag of the main tag
    const h1Title = main.getElementsByTagName('h1');
    const mainDescription = main.getElementsByTagName('p');
    const selectElement = document.createElement("select");

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
            
            const options = [{
                value: 'option1',
                text: 'Option 1'
            }, {
                value: 'option2',
                text: 'Option 2'
            }, {
                value: 'option3',
                text: 'Option 3'
            }]
            
            const select_onchange_functionality = function() {
                const selectedOption = selectElement.value;

                loadQueryOne(selectedOption).then(r => {
                    rowDiv[0].removeChild(loading)
                    chart = new Chart(
                        document.getElementById('chart'),
                        r
                    );
                });
            };
            
            addSelectElement(selectElement, mainDescription[0], options, select_onchange_functionality);

            break;
        case '#query2':
            h1Title[0].innerHTML = 'Query 2';
            mainDescription[0].innerHTML = 'Lorem others';

            loadQueryTwo(loading).then(r => {
                rowDiv[0].removeChild(loading)
                chart = new Chart(document.getElementById('chart'), r);
            });

            break;
        case '#query3':
            h1Title[0].innerHTML = 'Query 3';
            mainDescription[0].innerHTML = 'Lorem others';
            loadMap().then(LaMap => {
                loadQueryThree(LaMap).then(r => {
                    rowDiv[0].removeChild(loading)
                    Chart.register(ChoroplethController, GeoFeature, ColorScale, ProjectionScale);
                    chart = new Chart(document.getElementById('chart').getContext('2d'), r);
                });
            });
            break;
        default:
            loadQueryOne(loading).then(r => rowDiv[0].removeChild(loading));
            break;
    }
};


