google.charts.load('current', {'packages':['bar', 'corechart']});
google.charts.setOnLoadCallback(
    function() {
        drawChart1();
    });

function drawChart1() {
    var data = google.visualization.arrayToDataTable([
        ['Year', 'inoccupation', 'Elementary', 'middle', 'high', 'University'],
        ['2014', 10, 1000, 400, 200, 30],
        ['2015', 30, 1170, 460, 250, 500],
        ['2016', 40, 660, 1120, 300, 200],
        ['2017', 80, 1030, 540, 350, 700]
    ]);

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

function drawChart2() {

    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Work',     11],
        ['Eat',      2],
        ['Commute',  2],
        ['Watch TV', 2],
        ['Sleep',    7]
    ]);

    var options = {
        title: 'My Daily Activities',
        chartArea:{left:50,top:50,width:'100%',height:'100%'}
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

function drawChart3() {
    var data = google.visualization.arrayToDataTable([
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
    ]);

    var options = {
      title: 'Age vs. Weight comparison',
      hAxis: {title: 'Age', minValue: 0, maxValue: 15},
      vAxis: {title: 'Weight', minValue: 0, maxValue: 15},
      legend: 'none'
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}

function drawChart4() {
    var data = google.visualization.arrayToDataTable([
      ['Mon', 20, 28, 38, 45],
      ['Tue', 31, 38, 55, 66],
      ['Wed', 50, 55, 77, 80],
      ['Thu', 77, 77, 66, 50],
      ['Fri', 68, 66, 22, 15]
      // Treat first row as data as well.
    ], true);

    var options = {
      legend:'none'
    };

    var chart = new google.visualization.CandlestickChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}