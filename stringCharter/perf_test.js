var iters = 10000
function drawRectD3(){
    var draw = SVG().addTo('#contentDiv').size(3000, 3000);
    for (var i = 0; i < iters; i++) {
        var rect = draw.rect(100+i/2, 100+i/2).attr({ fill: '#f06' });
    }
}

function drawRectTwo(){
    var container = document.getElementById('svgContainer');
    var params = { width: 3000, height: 3000, type: Two.Types.svg};
    var two = new Two(params).appendTo(container);

    for (var i = 0; i < iters; i++) {
        var rect = two.makeRectangle(213, 100, 100, 100);
        rect.fill = 'rgb(0, 200, 255)';
        two.update();
    }
}

function drawRectWebgl(){
    var container = document.getElementById('svgContainer');
    var params = { width: 3000, height: 3000, type: Two.Types.webgl};
    var two = new Two(params).appendTo(container);

    for (var i = 0; i < iters; i++) {
        var rect = two.makeRectangle(213, 100, 100, 100);
        rect.fill = 'rgb(0, 200, 255)';
        two.update();
    }
}