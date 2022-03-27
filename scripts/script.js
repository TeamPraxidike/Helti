var bottomap = L.map('map').setView([42.50, 27.47388], 14.40);
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 20,
	attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
}).addTo(bottomap);

var maskIcon = L.icon({
    iconUrl: '/images/mask_v2.png',
    // shadowUrl: 'leaf-shadow.png',

    iconSize: [50, 50], 
    // shadowSize: [50, 64], 
    iconAnchor: [25, 50], 
    shadowAnchor: [4, 62],  
    popupAnchor: [0, -30] 
});

var vaxIcon = L.icon({
    iconUrl: '/images/vaxx_v2.png',
    iconSize: [50, 50],
    iconAnchor: [25, 50], 
    shadowAnchor: [4, 62],  
    popupAnchor: [0, -30] 
});

var covidCenter = L.icon({
    iconUrl: '/images/plus.png',
    iconSize: [50, 50],
    iconAnchor: [25, 50], 
    shadowAnchor: [4, 62],  
    popupAnchor: [0, -30] 
});



// Add some other locations like pharmacies.
let marker1 = new L.Marker([42.50800,27.47230], {icon: maskIcon});
marker1.addTo(bottomap).bindPopup(`<p>Мястото е Аптека Фарма Груп, Лазур</p> <img src="/images/aptekalazur.png" alt="" style="width: 200px;">`);

let marker2 = new L.Marker([42.51090,27.46970], {icon: maskIcon});
marker2.addTo(bottomap).bindPopup(`<p>Мястото е Аптека Мидея, Лазур</p> <img src="/images/аптекадопето5.png" alt="" style="width: 200px;">`);

let marker3 = new L.Marker([42.50360,27.47240], {icon: maskIcon});
marker3.addTo(bottomap).bindPopup(`<p>Мястото е Аптека Фармар, в <br> близост до ОУ "Васил Априлов"</p> <img src="/images/аптекадовасила.png" alt="" style="width: 200px;">`);

let marker4 = new L.Marker([42.50028,27.47152], {icon: maskIcon});
marker4.addTo(bottomap).bindPopup(`<p>Мястото е книжарницата <br> на гимназия ППМГ</p> <img src="/images/Screenshot_5.png" alt="" style="width: 200px;">`);

let marker5 = new L.Marker([42.51398,27.46652], {icon: vaxIcon});
marker5.addTo(bottomap).bindPopup(`<p>Мястото е център за ваксиниране <br> до УМБАЛ Бургас </p> <img src="/images/umbal.png" alt="" style="width: 200px;">`);

let marker6 = new L.Marker([42.50765,27.46782], {icon: covidCenter});
marker6.addTo(bottomap).bindPopup(`<p>Мястото е Военна болница </p> <img src="/images/dkz.png" alt="" style="width: 200px;">`);

let marker7 = new L.Marker([42.50950,27.46950], {icon: covidCenter});
marker7.addTo(bottomap).bindPopup(`<p>Мястото е "Ел Масри", Лазур</p> <img src="/images/elmasri.png" alt="" style="width: 200px;">`);

let marker8 = new L.Marker([42.52050,27.44440], {icon: vaxIcon});
marker8.addTo(bottomap).bindPopup(`<p>Мястото е МЦ II Бургас</p> <img src="/images/random2.png" alt="" style="width: 200px;">`);

let marker9 = new L.Marker([42.49425,27.46106], {icon: vaxIcon});
marker9.addTo(bottomap).bindPopup(`<p>Мястото е МЦ Европейска здравна грижа</p> <img src="/images/kalata.png" alt="" style="width: 200px;">`);

let marker10 = new L.Marker([42.50425,27.46106], {icon: vaxIcon});
marker10.addTo(bottomap).bindPopup(`<p>Мястото е МЦ Европейска здравна грижа</p> <img src="/images/bolnica1.png" alt="" style="width: 200px;">`);


// ? Changes begin here:

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jul 2021', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan 2022', 'Feb', 'Mar'],
        datasets: [{
            label: 'Total cases',
            data: [7700, 22386, 42020, 82910, 113229, 95207, 200142, 261402, 189243],
            borderColor: '#76282f',
            fill: false,
            tension: 0.4
        }]
    },
    options: {
        scales: {
            xAxis: {
                ticks: {
                    display: true
                },
                grid: {
                    display: false
                }
            },
            yAxis: {
                ticks: {
                    display: true
                },
                grid: {
                    display: false
                }
            }
        },
        plugins: {
            title: {
                display: true,
                text: 'Number of active cases in Bulgaria for every 25th day of the month'
            },
            legend: {
              display: false,
            },
            tooltip: {
                displayColors: false
            }
        },
        elements: {
            point: {
                radius: 1,
                hoverRadius: 4,
                backgroundColor: '#76282f'
            }
        }
    }
});
