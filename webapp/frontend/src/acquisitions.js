import Chart from 'chart.js/auto'
import {ChoroplethController, GeoFeature, ColorScale, ProjectionScale, topojson} from 'chartjs-chart-geo';


(async function() {
    const data = await fetch("http://localhost:8081/api/v1/business/").then(response => response.json())

    new Chart(
        document.getElementById('acquisitions'),
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
                    },{
                        label: '2022',
                        data: data.map(row => row.numBusinesses22),
                    }
                ]
            }
        }
    );
})();


(async function () {
    const us = await fetch('https://gist.githubusercontent.com/jonsadka/c1f75dfceeac5947da9b316469753b16/raw/7ddfde4e0709d07f369a1df951a776c27706639f/la.json').then((r) => r.json());

    const crime_data = await fetch("http://localhost:8081/api/v1/business/count").then(response => response.json())

    // const business_data = await fetch("http://localhost:8081/api/v1/business/").then(response => response.json())
    // console.log(business_data)
    //
    // const nation = topojson.feature(us, us.objects.nation).features[0];
    // const states = topojson.feature(us, us.objects.states).features;
    // let counties = topojson.feature(us, us.objects.counties).features;

    // const counties_from_business_data = business_data.map(row => row.cityName.toLowerCase())
    //
    // counties = counties.filter(
    //     (d) => counties_from_business_data.includes(d.properties.name.toLowerCase())
    // )
    console.log(crime_data)
    // console.log(counties_from_business_data, counties)
    const data = {
        labels: us.features.map(row => row.properties.name),
        datasets: [
            // {
            //     label: 'States',
            //     outline: nation,
            //     data: states.map((d) => ({
            //         feature: d,
            //         value: Math.random() * 11,
            //     })),
            // },
            {
                label: 'Counties',
                outline: us.features,
                data: us.features.map((d) => ({
                    feature: d,
                    value: crime_data.filter(row => row.area_name.trim() === d.properties.name).length > 0
                        ? crime_data.filter(row => row.area_name.trim() === d.properties.name)[0]["count"]
                        : 0,
                })),
            },
        ],
    };

    const config = {
        type: 'choropleth',
        data,
        options: {
            scales: {
                projection: {
                    axis: 'x',
                    projection: 'albersUsa',
                },
                color: {
                    axis: 'x',
                    quantize: 5,
                    legend: {
                        position: 'bottom-right',
                        align: 'right',
                    },
                },
            },
        },
    };

    Chart.register(ChoroplethController, GeoFeature, ColorScale, ProjectionScale);

    new Chart(document.getElementById('acquisitions2').getContext('2d'), config);

})();
