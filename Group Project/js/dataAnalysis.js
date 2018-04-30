// helper function to find the top n varieties of wine
function getTopVarieties(data, n){
  // Get unique varieties and occurances
  var varieties = []
  data.forEach(function(d) {
    if(!(d.variety in varieties)){
      varieties[d.variety] = 1;
    } else{
      varieties[d.variety] += 1;
    }
  });
  // Sort the values in descending order and select top 10
  var sorted = [];
  for (var v in varieties) {
    sorted.push([v, varieties[v]]);
  }
  sorted.sort(function(a, b) {
    return b[1] - a[1];
  });
  return sorted.slice(0,n);
};

// helper function to easily filter outliers
function filterOutliers(someArray) {
  // Copy the values, rather than operating on references to existing values
  var values = someArray.concat();

  // Then sort
  values.sort( function(a, b) {
    return a - b;
  });

  /* Then find a generous IQR. This is generous because if (values.length / 4)
  * is not an int, then really you should average the two elements on either
  * side to find q1.
  */
  var q1 = values[Math.floor((values.length / 4))];
  // Likewise for q3.
  var q3 = values[Math.ceil((values.length * (3 / 4)))];
  var iqr = q3 - q1;

  // Then find min and max values
  var maxValue = q3 + iqr*1.5;
  var minValue = q1 - iqr*1.5;

  // Then filter anything beyond or beneath these values.
  var filteredValues = values.filter(function(x) {
    return (x <= maxValue) && (x >= minValue);
  });

  // Then return
  return filteredValues;
}
