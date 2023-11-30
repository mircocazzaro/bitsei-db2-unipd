import Chart from "chart.js/auto";
import {ChoroplethController, GeoFeature, ColorScale, ProjectionScale, topojson} from 'chartjs-chart-geo';


// (async function() {
//     const data = await fetch("http://localhost:8081/api/v1/business/").then(response => response.json())
//
//     new Chart(
//         document.getElementById('acquisitions'),
//         {
//             type: 'bar',
//             data: {
//                 labels: data.map(row => row.cityName),
//                 datasets: [
//                     {
//                         label: '2020',
//                         data: data.map(row => row.numBusinesses20),
//                     }, {
//                         label: '2021',
//                         data: data.map(row => row.numBusinesses21),
//                     },{
//                         label: '2022',
//                         data: data.map(row => row.numBusinesses22),
//                     }
//                 ]
//             }
//         }
//     );
// })();

//
// (async function () {
//     const us = await fetch('https://gist.githubusercontent.com/farzad-845/1113f0eca0935a55a84ce6a51c5f7161/raw/5a83aa993db1e6da755320669d69d3e5cacf245b/LosAngeles.json').then((r) => r.json());
//     const us1 = await fetch('https://gist.githubusercontent.com/jonsadka/c1f75dfceeac5947da9b316469753b16/raw/7ddfde4e0709d07f369a1df951a776c27706639f/la.json').then((r) => r.json());
//     const us2 = await fetch("https://cdn.jsdelivr.net/npm/us-atlas/states-10m.json").then((r) => r.json());
//
//
//     // whole US for the outline
//     const nation = topojson.feature(us2, us2.objects.nation).features[0];
// // individual states
//     const states = topojson.feature(us2, us2.objects.states).features;
//
//     // const crime_data = await fetch("http://localhost:8081/api/v1/business/count").then(response => response.json())
//
//     // const business_data = await fetch("http://localhost:8081/api/v1/business/").then(response => response.json())
//     // console.log(business_data)
//     //
//     // const nation = topojson.feature(us, us.objects.nation).features[0];
//     // const states = topojson.feature(us, us.objects.states).features;
//     const counties = topojson.feature(us1, us1).features;
//     // console.log(counties)
//
//     // const counties_from_business_data = business_data.map(row => row.cityName.toLowerCase())
//     //
//     // counties = counties.filter(
//     //     (d) => counties_from_business_data.includes(d.properties.name.toLowerCase())
//     // )
//     // console.log(crime_data)
//     console.log(counties)
//
//     const data = {
//         labels: us1.features.map(row => row.properties.name),
//         datasets: [
//             {
//                 label: 'counties',
//                 outline: counties,
//                 data: counties.map((d) => ({
//                     feature: d,
//                     value: Math.random() * 11,
//                 })),
//             },
//             // {
//             //     label: 'Counties',
//             //     outline: us1.features,
//             //     data: us1.features.map((d) => ({
//             //         feature: d.properties.name,
//             //         value: 100000,
//             //     })),
//             // },
//         ],
//     };
//
//     // const data = {
//     //     labels: ['Alaska', 'California'],
//     //     datasets: [{
//     //         label: 'States',
//     //         outline: nation, // ... outline to compute bounds
//     //         showOutline: true,
//     //         data: [
//     //             {
//     //                 value: 0.4,
//     //                 feature: alaska // ... the feature to render
//     //             },
//     //             {
//     //                 value: 0.3,
//     //                 feature: california
//     //             }
//     //         ]
//     //     }]
//     // };
//
//     const config = {
//         type: 'choropleth',
//         data,
//         options: {
//             scales: {
//                 projection: {
//                     axis: 'x',
//                     projection: 'albersUsa',
//                 },
//                 color: {
//                     axis: 'x',
//                     quantize: 5,
//                     legend: {
//                         position: 'bottom-right',
//                         align: 'right',
//                     },
//                 },
//             },
//         },
//     };
//
//     Chart.register(ChoroplethController, GeoFeature, ColorScale, ProjectionScale);
//
//     new Chart(document.getElementById('chart').getContext('2d'), config);
//
// })();



(async function () {
    // const us = await fetch('https://gist.githubusercontent.com/jonsadka/c1f75dfceeac5947da9b316469753b16/raw/7ddfde4e0709d07f369a1df951a776c27706639f/la.json').then((r) => r.json());
    let us = await fetch('https://gist.githubusercontent.com/farzad-845/1113f0eca0935a55a84ce6a51c5f7161/raw/f3d3d4f546f7ae93af5e6591cd6c8f77fe6ecc52/LA.json').then((r) => r.json());

    const data = {
        labels: us.features.map(row => row.properties.NAME_ALF),
        datasets: [
            {
                label: 'Counties',
                outline: us.features,
                data: us.features.map((d) => ({
                    feature: d,
                    value: Math.random() * 100,
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
    };

    Chart.register(ChoroplethController, GeoFeature, ColorScale, ProjectionScale);

    new Chart(document.getElementById('chart').getContext('2d'), config);

})();