function drawLine(){
    // draw a simple line
    var width = 300;
    var height = 300;
    var svg = d3.select("#svgContainer")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
    svg.append("line")
        .attr("x1", 100)
        .attr("y1", 100)
        .attr("x2", 200)
        .attr("y2", 200)
        .style("stroke", "rgb(255,0,0)")
        .style("stroke-width", 2);

    return svg;
}

// set the dimensions and margins of the graph
// var margin = {top: 10, right: 40, bottom: 30, left: 30},
// width = 450 - margin.left - margin.right,
// height = 400 - margin.top - margin.bottom;
var margin = {top: 150, right: 200, bottom: 250, left: 200}, // if margins/height/width not set correctly, export svg doesnt work well
width = window.innerWidth - margin.left - margin.right, // Use the window's width 
height = 2400 - margin.top - margin.bottom; // Use the window's height
var line_colour = "black"

function tickSelector(i, labels){
    return labels[i];
}

// var svg;
function changeLineColor(line_colour){
    d3.selectAll("path")
    .filter(function(d, i) { return i > 3; })
    .transition()
    .duration(500)
    .attr("stroke", line_colour)
    .attr("fill", "none")
}
function getLineColour(line_colour){
    this.line_colour = line_colour
    console.log(line_colour)
}

function drawGraph(line_colour){
    // console.log(data[0])
    // This function is called by the buttons on top of the plot
    var schedule = [["Flughafen Wien Bahnhof", 6],["Wien Hbf", 7],["Wien Meidling Bahnhof", 8.5],["Wr.Neustadt Hbf", 13],["Semmering Bahnhof", 15],["Murzzuschlag Bahnhof", 16.5],["Kapfenberg Bahnhof", 18.3],["Bruck/Mur Bahnhof", 19], ["Graz Hbf", 20]];
    var stations = ["Flughafen Wien Bahnhof","Wien Hbf","Wien Meidling Bahnhof","Wr.Neustadt Hbf","Semmering Bahnhof","Murzzuschlag Bahnhof","Kapfenberg Bahnhof","Bruck/Mur Bahnhof", "Graz Hbf"]

    // append the svg object to the body of the page
    var svg = d3.select("#contentDiv")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // X scale and Axis
    var x = d3.scaleLinear()
    .domain([0, stations.length])         // This is the min and the max of the data: 0 to 100 if percentages
    .range([0, width]);       // This is the corresponding value I want in Pixels

    var tick_positions = [];
    var dataset = [];
    var dataset2 = [];
    for (i=0; i<stations.length;i++){
        var x_pt = (schedule[i][1] - 6) / 14 * stations.length;
        tick_positions.push(x_pt);
        dataset.push([x_pt, schedule[i][1], schedule[i][0]]) //append(x,y,stn name)
        dataset2.push([x_pt, schedule[i][1]+2, schedule[i][0]])
    }
    dataset2[2][1] = 12
    dataset2[5][1] += 0.7

    // console.log(tick_positions)
    var xlabels = stations;//['Wien Flughafen','Wien hbf','Graz hbf'];
    var x_axis = d3.axisBottom().scale(x).tickValues(tick_positions).tickFormat(function (d) {return xlabels[tick_positions.indexOf(d)];});
    // var x_axis_top = d3.axisTop().scale(x).tickValues(tick_positions).tickFormat(function (d) {return xlabels[tick_positions.indexOf(d)];});

    svg.append('g')
    .attr("transform", "translate(0," + height + ")")
    .call(x_axis)
    .selectAll("text")
    .style("text-anchor", "end")
    .attr("dx", "-.88em")
    .attr("dy", "-.5em")
    .attr("transform", "rotate(-90)");;

    svg.append('g')
    .call(x_axis)
    .selectAll("text")  
    .style("text-anchor", "end")
    .attr("dx", "-.88em")
    .attr("dy", "-.5em") //1em
    .attr("transform", "rotate(90)");


    // Y scale and Axis
    var y = d3.scaleLinear()
    .domain([0, 24])         // This is the min and the max of the data: 0 to 100 if percentages
    .range([height, 0]);       // This is the corresponding value I want in Pixel

    var y_axis_left = d3.axisLeft().scale(y).tickFormat(function (d) {return d + ":00";});
    var y_axis_right = d3.axisRight().scale(y).tickFormat(function (d) {return d + ":00";});
    svg.append('g')
    .attr("transform", "translate(" + width + ", 0)")
    .call(y_axis_right);

    svg.append('g')
    .call(y_axis_left);


    // Draw line
    
    // 7. d3's line generator
    // var stations = ["Flughafen Wien Bahnhof","Wien Hbf","Wien Meidling Bahnhof","Wr.Neustadt Hbf","Semmering Bahnhof","Murzzuschlag Bahnhof","Kapfenberg Bahnhof","Bruck/Mur Bahnhof"]
    // var times = []
    // var dataset = [["Flughafen Wien Bahnhof", 6],["Wien Hbf", 7],["Wien Meidling Bahnhof", 8.5],["Wr.Neustadt Hbf", 13],["Semmering Bahnhof", 15],["Murzzuschlag Bahnhof", 16.5],["Kapfenberg Bahnhof", 18.3],["Bruck/Mur Bahnhof", 19], ["Graz Hbf", 20]];
    var line = d3.line()
    .x(function(d) { return x(d[0]); }) // set the x values for the line generator
    .y(function(d) { return y(d[1]); });

    // 9. Append the path, bind the data, and call the line generator
    var trips = [dataset, dataset2];
    for (i=0; i<trips.length;i++){
        svg.append("path")
        .attr("stroke", line_colour)
        .attr("fill", "none")
        .attr("d", line(trips[i])); // 11. Calls the line generator 
    }

    function floatToTime(num){
        // console.log(num)
        // console.log(moment().startOf('day').add(parseFloat(num), "hours").format("HH:mm"))
        return " "+ moment().startOf('day').add(parseFloat(num), "hours").format("HH:mm");
    }

    // dots
    var dot_size = 3.5;
    svg.selectAll(".dot")
    .data(dataset.concat(dataset2))
    .enter().append("circle") // Uses the enter().append() method
        .attr("class", "dot") // Assign a class for styling
        .attr("fill", "black")
        .attr("cx", function(d) { return x(d[0]) })
        .attr("cy", function(d) { return y(d[1]) })
        .attr("r", dot_size)

        // tooltip on hover
        .on('mouseover', function (d, i) {
            let tooltip = d[2] + floatToTime(d[1]);
            d3.text(tooltip);
            d3.select(this).transition()
                 .duration('50')
                 .attr('opacity', '.3')
                 .attr('r', dot_size+2.5);
       })     .on('mouseout', function (d, i) {
            d3.select(this).transition()
                 .duration('50')
                 .attr('opacity', '1')
                 .attr("r", dot_size);
       })
       .append("svg:title")
       .text(function(d) { return d[2] + floatToTime(d[1]); });

    return svg;
}


function saveAsSVG() {
    var svgString = getSVGString(svg.node());
    var svg_text = new Blob([svgString],
        { type: "image/svg+xml;charset=utf-8" }); // type:"text/svg;charset=utf-8"
    saveAs(svg_text, "test.svg");
}

// https://stackoverflow.com/questions/23218174/how-do-i-save-export-an-svg-file-after-creating-an-svg-with-d3-js-ie-safari-an
function getSVGString(svgNode){
    const xmlns = "http://www.w3.org/2000/xmlns/";
    const xlinkns = "http://www.w3.org/1999/xlink";
    const svgns = "http://www.w3.org/2000/svg";
    var svgString = svgNode.innerHTML; // inner or outer html? svg

    //add name spaces.
    svgString = "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" >" + svgString + "</svg>";
    return svgString;
}

var openFile = function(event) {
    var input = event.target;
    console.log(input.files[0]);

    d3.csv(input.files[0].path).then(function(data) {
        drawGraph(data)
        // //GET ALL DATA FROM CSV HERE
        // console.log(data[0]);
        // console.log(data[1]);
      });
  };
