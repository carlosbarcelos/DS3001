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
    makeOverallPieChart(data);
    makeVarietiesPieChart(data);
  });
};

// Create the country pie chart
function makeOverallPieChart(data){
  // Get unique varieties and occurances
  var countries = []
  data.forEach(function(d) {
    if(!(d.country in countries)){
      countries[d.country] = 1;
    } else{
      countries[d.country] += 1;
    }
  });
  var countryList = [];
  for (var c in countries) {
    countryList.push([c, countries[c]]);
  }
  // Create the plot data by ...
  var labels = [];
  var values = [];
  // ... collecting data points ...
  var i;
  for (i = 0; i < 10; i++) {
      labels.push(countryList[i][0]);
      values.push(countryList[i][1]);
  }

  // ... adding to chart
  var plotData = [{
    values: values,
    labels: labels,
    type: 'pie'
  }];

  // Put chart on page
  var layout = {
    title: 'Individual Country Marketshare'
  };
  Plotly.newPlot('piechart', plotData, layout);
};

// Create the price / variety boxplot
function makeVarietiesPieChart(data){


  // For each of the top ten varieties...
  var topVarieties = getTopVarieties(data, 3);
  var plotData = [];
  var outputLocations = ['piechart-varieties1','piechart-varieties2','piechart-varieties3'];
  var cnt = 0;
topVarieties.forEach(function(topD) {
    // Get the country list for this Variety
    var countries = []
    data.forEach(function(d) {
      if(topD[0] == d.variety){
        if(!(d.country in countries)){
          countries[d.country] = 1;
        } else{
          countries[d.country] += 1;
        }
      }
    });
    var countryList = [];
    for (var c in countries) {
      countryList.push([c, countries[c]]);
    }

    // Create the plot data by ...
    var labels = [];
    var values = [];
    // ... collecting data points ...
    var i;
    for (i = 0; i < 10; i++) {
        labels.push(countryList[i][0]);
        values.push(countryList[i][1]);
    }
    // ... adding to chart
    var plotData = [{
      values: values,
      labels: labels,
      type: 'pie'
    }];
    // Put chart on page
    var layout = {
      title: 'Individual Country Marketshare (' + topD[0] + ')',
      height: 400,
      width: 500
    };
    Plotly.newPlot(outputLocations[cnt++], plotData, layout);
  });
};

performAnalysis();
