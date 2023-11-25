import Chart from "chart.js/auto";

function loadQueryOne() {
    fetch("http://127.0.0.1:8080/api/v1/business/")
        .then(response => response.json())
        .then(data => {
            new Chart(
                document.getElementById('chart'),
                {
                    type: 'bar',
                    data: {
                        labels: data.map(row => row.cityName),
                        datasets: [
                            {
                                label: '2020',
                                data: data.map(row => row.numBusinesses20),
                            }, {
                                label: '2021',
                                data: data.map(row => row.numBusinesses21),
                            }, {
                                label: '2022',
                                data: data.map(row => row.numBusinesses22),
                            }
                        ]
                    }
                }
            );
        })
        .catch(error => {
            console.error(error)
        });
}


export {loadQueryOne};