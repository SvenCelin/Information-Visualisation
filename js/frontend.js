//currently hardcoded
var query = {
    days: "Weekdays", //true means weekdays or simply all?
    direction : "GrazVienna",
    timeFrom : 0,
    timeTo : 24,
    color : "#696969"
};

function setDays(value){
    query.days = value;

}

function setDirection(value){
    query.direction = value;
}

function setTimeFrom(value){
    query.timeFrom = value;
}

function setTimeTo(value){
    query.timeTo = value;
}


function setColor(value){
    query.color = value;
}




function exportSVG() {
    //ToDo: this should promt an SVG download

    console.dir(query);
} 