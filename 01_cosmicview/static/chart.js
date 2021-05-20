// We will use CDN of lightweight-chart in HTML

// Candlestick

var chart = LightweightCharts.createChart(document.getElementById('chart'), {
    width: 800,
    height: 600,
    layout: {
        backgroundColor: '#000000',
        textColor: 'rgba(255, 255, 255, 0.9)',
    },
    grid: {
        vertLines: {
            color: 'rgba(197, 203, 206, 0.5)',
        },
        horzLines: {
            color: 'rgba(197, 203, 206, 0.5)',
        },
    },
    crosshair: {
        mode: LightweightCharts.CrosshairMode.Normal,
    },
    rightPriceScale: {
        borderColor: 'rgba(197, 203, 206, 0.8)',
    },
    timeScale: {
        borderColor: 'rgba(197, 203, 206, 0.8)',
    },
});

var candleSeries = chart.addCandlestickSeries({
    upColor: 'rgba(50, 205, 50, 1)',
    downColor: 'rgb(220,20,60)',
    borderDownColor: 'rgba(255, 144, 0, 1)',
    borderUpColor: 'rgba(255, 144, 0, 1)',
    wickDownColor: 'rgba(220,20,60, 1)',
    wickUpColor: 'rgba(50, 205, 50, 1)',
});

// fetch function to get data from backend


// Go to developer tools Network >> history >> response to see if data is coming in
fetch('http://localhost:5000/history')
    .then((r) => r.json())
    .then((response) => {
        console.log(response)

        candleSeries.setData(response);
    })
// Simple chart
/* const chart = LightweightCharts.createChart(document.getElementById('chart'), {
    width: 400,
    height: 300
});
const lineSeries = chart.addLineSeries();
lineSeries.setData([{time: '2019-04-11',value: 80.01},
    {time: '2019-04-12',value: 96.63},
    {time: '2019-04-13',value: 76.64},
    {time: '2019-04-14',value: 81.89},
    {time: '2019-04-15',value: 74.43},
    {time: '2019-04-16',value: 80.01},
    {time: '2019-04-17',value: 96.63},
    {time: '2019-04-18',value: 76.64},
    {time: '2019-04-19',value: 81.89},
    {time: '2019-04-20',value: 74.43},
]); */