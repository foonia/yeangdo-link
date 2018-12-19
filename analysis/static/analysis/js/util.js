window.onload = function() {
    requestData(add_row);

    var occupationSelect = document.getElementById('occupationSelect');
    console.log(occupationSelect);
    occupationSelect.addEventListener('change', function() {
        refreshOccupation(add_row);
    }, false)
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
        row.insertCell(6).innerHTML = value.phone;

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


function refreshOccupation(callback) {
    var req = new XMLHttpRequest();

    $("#my-tbody").empty();
    var occupation = document.getElementById('occupationSelect').value;

    req.addEventListener('load', function(){
        var jsonData = JSON.parse(req.responseText);
        var results = jsonData['results'];
        var next = jsonData['next'];
        var previous = jsonData['previous'];

        callback(results);
    });

    req.open('GET', '/api/survey/?occupation=' + occupation);
    req.send(null);
}

