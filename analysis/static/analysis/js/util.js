window.onload = function() {
    requestData(add_row);
};


function add_row(surveyData) {

    var tbody = document.getElementById('my-tbody');

    surveyData.map(function(value){
        var row = tbody.insertRow(-1);

        row.insertCell(0).innerHTML = value.id;
        row.insertCell(1).innerHTML = value.sex;
        row.insertCell(2).innerHTML = value.final_education;
        row.insertCell(3).innerHTML = value.desired_occupation1;
        row.insertCell(4).innerHTML = value.desired_salary;
        row.insertCell(5).innerHTML = value.address;
    });



}


function requestData(callback) {
    var req = new XMLHttpRequest();

    req.addEventListener('load', function(){
        var jsonData = JSON.parse(req.responseText);
        var results = jsonData['results'];
        var next = jsonData['next'];
        var previous = jsonData['previous'];

        callback(results);
    });

    req.open('GET', '/api/survey/');
    req.send(null);
}

