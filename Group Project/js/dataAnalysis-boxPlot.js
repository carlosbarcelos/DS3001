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
    makePriceBoxPlot(data);
  });
};

// Create the price / variety boxplot
function makePriceBoxPlot(data){
  var topVarieties = getTopVarieties(data, 10);
  // For each of the top ten varieties...
  var plotData = [];
  topVarieties.forEach(function(topD) {
    var points = [];
    // ... collect data points ...
    data.forEach(function(d) {
      if(topD[0] == d.variety){
        points.push(d.price);
      }
    });
    // ... remove outliers ...
    points = filterOutliers(points);
    // ... add to chart.
    var trace = {
      y: points,
      type: 'box',
      boxpoints: false,
      name: topD[0]
    };
    plotData.push(trace);
  });

  // Put chart on page
  var layout = {
    title: 'Accurate Wine Pricing',
    xaxis: {title: 'Variety'},
    yaxis: {title: 'Price'}
  };
  Plotly.newPlot('boxplot', plotData, layout);
};

performAnalysis();
