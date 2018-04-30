apiData = {};
locations = [];
var i;
var apiKeys;
var data;
function pullData(i,  apiKeys, data){
  if (i==apiKeys.length){
    endProcess(data);
  }
  else{

    d3.json("https://maps.googleapis.com/maps/api/geocode/json?address="+apiKeys[i]+"&key=AIzaSyB4ygQCaubyD3_W1wqxQUAC76zN15WyxsM", (error, d)=>{
      if (error){
        console.log(error);
      }
      if (d['results'].length < 1){
        //console.log(i +": "+ apiKeys[i]);
        apiData [apiKeys[i]] = {'lat':0, 'lng': 0};
      }else{
        apiData [apiKeys[i]] = d['results'][0]['geometry']['location'];
    }
    wait(21);
    pullData( i+1, apiKeys, data);
    });

  }
}
function endProcess(data){
  apiKeys = Object.keys(apiData);
    txt = "data:text/csv;charset=utf-8,";
    for (i =0; i< data.length; i++){
      let lat = apiData[data[i]['key']]['lat'];
      let lng =apiData[data[i]['key']]['lng'];
    txt+=data[i]['country'] +','+ data[i]['points']+ ','+ data[i]['price'] +',"'+ data[i]['province']	+'","'+ (data[i]['title'])+'","'+ data[i]['variety']+'","'+ data[i]['description']+'","'+ data[i]['region_1'] +'","'+ data[i]['winery']+'",'+lat+','+ lng+'\r\n';
    }
    console.log(txt);
    var encodedUri = encodeURI(txt);
    window.open(encodedUri);
}
function wait(ms)
{
var d = new Date();
var d2 = null;
do { d2 = new Date(); }
while(d2-d < ms);
}

d3.csv("ds3001/dataset/wineData_clean.csv", undefined,callback = function(error, inData) {
  data = inData;
  for (var i =0; i< data.length; i++){
    if (data[i]['region_1']=== ""){
      key = data[i]['country'];//last time province + country ran for no region and failed

    }else{
      key = data[i]['region_1']+","+ data[i]['country'];//no province names works as some confuse google (ex North East Italy)
    }
    if (  apiData [key] === undefined){
      apiData[key] = []
    }
    data[i]['key']= key;
    apiData [key].push(i);
  }
  var apiKeys = Object.keys(apiData);
  var q = d3.queue();
  i=0;
  pullData( i, apiKeys, data);
});
