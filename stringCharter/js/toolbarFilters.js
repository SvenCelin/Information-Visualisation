//currently hardcoded
var query = {
    direction : "GrazVienna",
    timeFrom : 0,
    timeTo : 24,
    color : "#696969",
    data : ""
};

function setDirection(value){
    query.direction = value;
}

function setTimeFrom(value){
    query.timeFrom = value;
    d3.csv(query.data).then(function (data) {
        svg_data = drawGraph(data)
    })
}

function setTimeTo(value){
    query.timeTo = value;
    d3.csv(query.data).then(function (data) {
        svg_data = drawGraph(data)
    })
}

function setColor(value){
    query.color = value;
}