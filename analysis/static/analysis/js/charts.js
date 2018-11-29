google.charts.load('current', {'packages':['bar', 'corechart']});
google.charts.setOnLoadCallback(
    function() {
        requestDrawChart(drawChart1, 'bar');
    });

function drawChart1(originData) {
    var data = google.visualization.arrayToDataTable(originData);

    var options = {
        chart: {
            title: '연령별 최종학력 현황',
            subtitle: 'Expression from 20s to 70s',
        },
        bars: 'vertical',
        vAxis: {format: 'decimal'},
        height: 400,
        colors: ['#1b9e77', '#d95f02', '#7570b3']
    };

    var chart = new google.charts.Bar(document.getElementById('chart_div'));

    chart.draw(data, google.charts.Bar.convertOptions(options));
}

function drawChart2(originData) {
    var data = google.visualization.arrayToDataTable(originData);

    var options = {
        title: 'My Daily Activities',
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

function drawChart3(originData) {
    var data = google.visualization.arrayToDataTable(originData);

    var options = {
      title: 'Company Performance',
      curveType: 'function',
      legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

function drawChart4(originData) {
    var data = google.visualization.arrayToDataTable(originData, true);

    var options = {
      legend:'none'
    };

    var chart = new google.visualization.CandlestickChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}