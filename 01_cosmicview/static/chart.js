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

// fetch function to get data from backend from python /history path that has data coming to it in json format
// Go to developer tools Network >> history >> response to see if data is coming in
fetch('http://localhost:5000/history')
    .then((r) => r.json())
    .then((response) => {
        console.log(response)

        candleSeries.setData(response);
    })

// Get data in real time using WSS

var binanceSocket = new WebSocket(
    "wss://stream.binance.com:9443/ws/btcusdt@kline_15m"
);



binanceSocket.onmessage = function (event) {
    console.log(event.data)


    var message = JSON.parse(event.data)
    // make new variable to be sent to chart
    var candlestick = message.k

    // update with time, open, high, low, close value to add to chart
    candleSeries.update({
        // time: Date.now(), // For Testing
        time: candlestick.t / 1000,
        open: candlestick.o,
        high: candlestick.h,
        low: candlestick.l,
        close: candlestick.c,
    })

    console.log(message.k)
}



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