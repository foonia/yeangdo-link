function requestDrawChart(callback, category) {
    var req = new XMLHttpRequest();

    req.addEventListener("load", function() {
        callback(JSON.parse(req.responseText));
    });

    req.open("GET", "/api/"+ category + "/");
    req.send(null);
}