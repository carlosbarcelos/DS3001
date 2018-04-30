var mayson = [{"Favorited": 94, "TotalTweets": 57, "Retweets": 92, "Wine": "Pinot Noir"}, 
              {"Favorited": 206, "TotalTweets": 200, "Retweets": 1358, "Wine": "Chardonnay"}, 
              {"Favorited": 207, "TotalTweets": 77, "Retweets": 353, "Wine": "Cabernet Sauvignon"}, 
              {"Favorited": 24, "TotalTweets": 9, "Retweets": 6, "Wine": "Red Blend"}, 
              {"Favorited": 3, "TotalTweets": 1, "Retweets": 0, "Wine": "Bordeaux-style Red Blend"}, 
              {"Favorited": 290, "TotalTweets": 200, "Retweets": 409, "Wine": "Riesling"}, 
              {"Favorited": 9, "TotalTweets": 10, "Retweets": 2, "Wine": "Sauvignon Blanc"}, 
              {"Favorited": 266, "TotalTweets": 200, "Retweets": 986, "Wine": "Syrah"}, 
              {"Favorited": 69, "TotalTweets": 200, "Retweets": 91736, "Wine": "Rose"}, 
              {"Favorited": 805, "TotalTweets": 200, "Retweets": 2189, "Wine": "Merlot"}]

// Create the bubble graph
function makeBubbleChart(){
  //Get unique varieties and occurances
  var winenames = []
  var favorites = []
  var tweets = []
  var favoriteRetweets = []
  var retweets = [];
  mayson.forEach(function(d) {
    winenames.push(d.Wine);
    tweets.push(d.TotalTweets);
    favorites.push(d.Favorited);
    favoriteRetweets.push("Favorited "+d.Favorited+" times. </br>Retweeted "+d.Retweets+" times.");
    retweets.push(d.Retweets);
  });

  //... adding to chart
  var trace = {
   x: winenames,
   y: tweets,
   text: favoriteRetweets,
   mode: 'markers',
   marker: {
     size: favorites,
     sizemode: 'area',
     sizeref: 0.15,
     color: retweets,
     colorscale: [[0, 'rgb(25, 150, 25)'], [1, 'rgb(150, 25, 150)']]
   }
  };

  var data = [trace];

  // Put chart on page
  var layout = {
   title: 'Twitter Popularity',
   xaxis: {title: 'Wine Variety'},
   yaxis: {title: 'Number of Tweets'}
  };

  Plotly.newPlot('bubblechart', data, layout);
};

makeBubbleChart();
