window.onload = function() {
    var btn1 = document.getElementById('chart1');
    var btn2 = document.getElementById('chart2');
    var btn3 = document.getElementById('chart3');
    var btn4 = document.getElementById('chart4');

    btn1.addEventListener("click", function() {
        requestDrawChart(drawChart1, 'bar');
    });

    btn2.addEventListener("click", function() {
        requestDrawChart(drawChart2, 'chart');
    });

    btn3.addEventListener("click", function() {
        requestDrawChart(drawChart3, 'curve');
    });

    btn4.addEventListener("click", function() {
        requestDrawChart(drawChart4, 'candle');
    });
};
