const URL_HOST = "https://gd.bitsei.it/api/v1"
function loadQueryOne() {
    return fetch(`${URL_HOST}/crime/category-month`)
        .then(response => response.json())
        .then(data => (
            {
                type: 'radar',
                data: {
                    labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                    datasets: data
                },
                options: {
                    responsive: true,
                }
            }
        )).catch(error => {
            console.error(error)
        });
}

function loadQueryTwo() {
    return fetch(`${URL_HOST}/business/open-closed-by-naics/`)
        .then(response => response.json())
        .then(data => (
            {
                type: 'bar',
                data: {
                    labels: data.map(row => row.naicsDesc),
                    datasets: [
                        {
                            label: 'closed',
                            data: data.map(row => row.closedBusinesses),
                        }, {
                            label: 'opened',
                            data: data.map(row => row.openedBusinesses),
                        }
                    ]
                }
            }
        )).catch(error => {
            console.error(error)
        });
}

function loadQueryThree(us) {
    return fetch(`${URL_HOST}/crime/category-event-by-area`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            return {
                type: 'choropleth',
                data: {
                    labels: us.features.map(row => row.properties.NAME_ALF),
                    datasets: [
                        {
                            label: 'Counties',
                            outline: us.features,
                            data: us.features.map((d) => ({
                                feature: d,
                                value: data.filter(mp => mp.acronym === d.properties.Acronym)[0].ratio,
                            })),
                        },
                    ],
                },
                options: {
                    scales: {
                        projection: {
                            axis: 'x',
                            projection: 'albersUsa',
                        },
                        color: {
                            interpolate: 'orRd',
                            axis: 'x',
                            quantize: 5,
                            legend: {
                                position: 'bottom-right',
                                align: 'right',
                            },
                        },
                    },
                },
            }
        }).catch(error => {
            console.error(error)
        });
}


function loadQueryFour() {
    return fetch(`${URL_HOST}/covid/cases_and_deaths`)
        .then(response => response.json())
        .then(data => (
            {
                type: 'line',
                data: {
                    labels: data.map(row => row.period),
                    datasets: [
                        {
                            label: 'Number of Covid Cases',
                            data: data.map(row => row.numOfCovidCases),
                            yAxisID: 'y',
                        }, {
                            label: 'Number of Deaths',
                            data: data.map(row => row.numOfDeaths),
                            yAxisID: 'y1',
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            type: 'linear',
                            display: true,
                            position: 'left',
                        },
                        y1: {
                            type: 'linear',
                            display: true,
                            position: 'right',

                            grid: {
                                drawOnChartArea: false, // only want the grid lines for one axis to show up
                            },
                        },
                    }
                }
            }
        )).catch(error => {
            console.error(error)
        });
}

function loadQueryFive(us, selectElementValue) {
    return fetch(`${URL_HOST}/crime/ratio-by-area?file_name=${selectElementValue}`)
        .then(response => response.json())
        .then(data => {
            return {
                type: 'choropleth',
                data: {
                    labels: us.features.map(row => row.properties.NAME_ALF),
                    datasets: [
                        {
                            label: 'Counties',
                            outline: us.features,
                            data: us.features.map((d) => ({
                                feature: d,
                                value: data.filter(mp => mp.acronym === d.properties.Acronym)[0].ratio,
                            })),
                        },
                    ],
                },
                options: {
                    scales: {
                        projection: {
                            axis: 'x',
                            projection: 'albersUsa',
                        },
                        color: {
                            interpolate: 'orRd',
                            axis: 'x',
                            quantize: 5,
                            legend: {
                                position: 'bottom-right',
                                align: 'right',
                            },
                        },
                    },
                },
            }
        }).catch(error => {
            console.error(error)
        });
}

function loadMap() {
    return fetch("https://gist.githubusercontent.com/farzad-845/1113f0eca0935a55a84ce6a51c5f7161/raw/f3d3d4f546f7ae93af5e6591cd6c8f77fe6ecc52/LA.json")
        .then(response => response.json())
        .catch(error => {
            console.error(error)
        });
}

export {loadQueryOne, loadQueryTwo, loadQueryThree, loadQueryFour, loadQueryFive, loadMap};

