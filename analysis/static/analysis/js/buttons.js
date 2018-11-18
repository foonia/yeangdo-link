window.onload = function() {
    var btn1 = document.getElementById('chart1');
    var btn2 = document.getElementById('chart2');
    var btn3 = document.getElementById('chart3');
    var btn4 = document.getElementById('chart4');

    btn1.addEventListener("click", function() {
        drawChart1();
    });

    btn2.addEventListener("click", function() {
        drawChart2();
    });

    btn3.addEventListener("click", function() {
        drawChart3();
    });

    btn4.addEventListener("click", function() {
        drawChart4();
    });
};
