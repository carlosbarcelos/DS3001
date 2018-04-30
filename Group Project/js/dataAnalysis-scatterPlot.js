// Read CSV and create graphs
function performAnalysis() {
  d3.csv("../dataset/wineData_CLEAN.csv", function(d) {
    return {
      country : d.country,
      points : +d.points,
      price : +d.price,
      province : d.province,
      variety : d.variety
    };
  }, function(data) {
    makePriceScatterPlot(data);
  });
};

// Create the price / quality scatterplot
function makePriceScatterPlot(data){
  var topVarieties = getTopVarieties(data, 5);
  // For each of the top ten varieties...
  var plotData = [];
  topVarieties.forEach(function(topD) {
    var xValues = [];
    var yValues = [];
    // ... collect data points ...
    data.forEach(function(d) {
      if(topD[0] == d.variety){
        xValues.push(d.price);
        yValues.push(d.points);
      }
    });
    // ... remove outliers ...
    xValues = filterOutliers(xValues);
    yValues = filterOutliers(yValues);
    // ... add to chart.
    var trace = {
      x: xValues,
      y: yValues,
      mode: 'markers',
      type: 'scatter',
      name: topD[0]
    };
    plotData.push(trace);
  });

  //Put chart on page
  var layout = {
    title: 'The Correlation of Wine Price and Quality',
    xaxis: {title: 'Price'},
    yaxis: {title: 'Quality'}
  };
  Plotly.newPlot('scatterplot', plotData, layout);
};

performAnalysis();
