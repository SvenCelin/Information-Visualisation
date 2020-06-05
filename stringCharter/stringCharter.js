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
var margin = {top: 50, right: 50, bottom: 50, left: 50},
width = (window.innerWidth - margin.left - margin.right)/2, // Use the window's width 
height = window.innerHeight - margin.top - margin.bottom; // Use the window's height


function drawGraph(){
    // append the svg object to the body of the page
    var svg = d3.select("#svgContainer")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // X scale and Axis
    var x = d3.scaleLinear()
    .domain([0, 100])         // This is the min and the max of the data: 0 to 100 if percentages
    .range([0, width]);       // This is the corresponding value I want in Pixel
    svg.append('g')
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

    // X scale and Axis
    var y = d3.scaleLinear()
    .domain([0, 100])         // This is the min and the max of the data: 0 to 100 if percentages
    .range([height, 0]);       // This is the corresponding value I want in Pixel
    svg.append('g')
    .call(d3.axisLeft(y));

    // svgstring = getSVGString(svg.node());
    // console.log(svgstring);
    return svg;
}


function saveAsSVG(svg) {
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

    var svgString = svgNode.outerHTML; // svg

    //add name spaces.
    svgString = "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">" + svgString + "</svg>";
    return svgString;
}


/* function getSVGStringAlt( svgNode ) {
    svgNode.setAttribute('xlink', 'http://www.w3.org/1999/xlink');
	var cssStyleText = getCSSStyles( svgNode );
	appendCSS( cssStyleText, svgNode );

	var serializer = new XMLSerializer();
    var svgString = serializer.serializeToString(svgNode);

	svgString = svgString.replace(/(\w+)?:?xlink=/g, 'xmlns:xlink='); // Fix root xlink without namespace
	svgString = svgString.replace(/NS\d+:href/g, 'xlink:href'); // Safari NS namespace fix
    
    // // Replace first <g xmlns with svg>
    // g_trans = "<g transform=\"translate(" + margin.left + "," + margin.top + ")\"><style xm";

    // svgString = svgString.replace("<style xm", g_trans); // left and top

    // // svg is replacede with g for some reason. change it back
    // svgString = svgString.replace("<g xmlns", "<svg xmlns");
    // svgString = svgString + "</svg>";
    // console.log("DGADF");
    // console.log(svgString);

	return svgString;

	function getCSSStyles( parentElement ) {
		var selectorTextArr = [];

		// Add Parent element Id and Classes to the list
		selectorTextArr.push( '#'+parentElement.id );
		for (var c = 0; c < parentElement.classList.length; c++)
				if ( !contains('.'+parentElement.classList[c], selectorTextArr) )
					selectorTextArr.push( '.'+parentElement.classList[c] );

		// Add Children element Ids and Classes to the list
		var nodes = parentElement.getElementsByTagName("*");
		for (var i = 0; i < nodes.length; i++) {
			var id = nodes[i].id;
			if ( !contains('#'+id, selectorTextArr) )
				selectorTextArr.push( '#'+id );

			var classes = nodes[i].classList;
			for (var c = 0; c < classes.length; c++)
				if ( !contains('.'+classes[c], selectorTextArr) )
					selectorTextArr.push( '.'+classes[c] );
		}

		// Extract CSS Rules
		var extractedCSSText = "";
		for (var i = 0; i < document.styleSheets.length; i++) {
			var s = document.styleSheets[i];
			
			try {
			    if(!s.cssRules) continue;
			} catch( e ) {
		    		if(e.name !== 'SecurityError') throw e; // for Firefox
		    		continue;
		    	}

			var cssRules = s.cssRules;
			for (var r = 0; r < cssRules.length; r++) {
				if ( contains( cssRules[r].selectorText, selectorTextArr ) )
					extractedCSSText += cssRules[r].cssText;
			}
		}
		

		return extractedCSSText;

		function contains(str,arr) {
			return arr.indexOf( str ) === -1 ? false : true;
		}

	}

	function appendCSS( cssText, element ) {
		var styleElement = document.createElement("style");
		styleElement.setAttribute("type","text/css"); 
		styleElement.innerHTML = cssText;
		var refNode = element.hasChildNodes() ? element.children[0] : null;
		element.insertBefore( styleElement, refNode );
	}
} */