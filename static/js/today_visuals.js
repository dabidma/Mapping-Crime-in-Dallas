// Creating our initial map object:
// We set the longitude, latitude, and starting zoom level.
// This gets inserted into the div with an id of "map".
let myMap = L.map("map", {
  center: [32.7767, -96.797],
  zoom: 10

});

// Adding a tile layer (the background map image) to our map:
// We use the addTo() method to add objects to our map.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);
if (today_data.length == 0){
  var popup = L.popup()
    .setLatLng([32.77, -96.79])
    .setContent("YAY! No drug arrests were made today!!!")
    .openOn(myMap);
  popup.addTo(myMap);
  console.log('no drug arrests')
} else{
  for (i=0; i<today_data.length;i++) {
    let item = month_data[i]
    console.log([item.lat, item.lon])
    let marker = L.marker([item.lat, item.lon], {
      draggable: false,
      title: "My First Marker"
    }).bindPopup(`${item.arladdress} <br> Arrest Time: ${item.ararrestdate}`).openPopup().addTo(myMap)
  };
};

if (today_data.length > 0){
  let today_drugs = today_data.map(data => data.drugtype).filter(data => data != null)
  let drugs=['Marijuana', 'Cocaine', 'Methamphetamine','Heroin','Hydrocone','Ectasy','Oxycodone', 'GHB', 'Ketamine','Other Prescription Drugs','Other Non-Prescription Drugs']
  let marijuana = 0;
  let meth = 0;
  let coke=0;
  let heroin=0;
  let otherPDrug=0;
  let otherNPdrug=0;
  let hydrocodone=0;
  let ectasy=0;
  let Oxycodone=0;
  let GHB=0;
  let Ketamine=0;

  for (let i=0; i<today_data.length; i++) {
    let item=month_data[i];
    
    if (item.drugtype == 'Cultivated Marijuana' || item.drugtype == 'Processed Marijuana' ){marijuana++} 
    else if (item.drugtype ==  'Methamphetamine'){meth++}
    else if (item.drugtype == 'Crack Cocaine' || item.drugtype == 'Powder Cocaine'){coke++}
    else if (item.drugtype == 'Heroin'){heroin++}
    else if (item.drugtype ==  'Other Prescription Drugs'){otherPDrug++}
    else if (item.drugtype ==  'Other Non-Prescription Drugs'){otherNPdrug++}
    else if (item.drugtype == 'Hydrocodone'){hydrocodone++}
    else if (item.drugtype == 'Ecstacy'){ectasy++}
    else if (item.drugtype == 'Oxycodone'){Oxycodone++}
    else if (item.drugtype == 'GHB'){GHB++}
    else if (item.drugtype == 'Ketamine'){Ketamine++}

    
  };

  let trace1 = {
    x: drugs,
    y: [marijuana,coke,meth,heroin,hydrocodone, ectasy, Oxycodone,GHB, Ketamine, otherPDrug,otherNPdrug],
    type: 'bar'
  };

  let data = [trace1];

  let layout = {
    title: "A Plotly plot"
  };

  Plotly.newPlot("chart1", data, layout);

}else {
  var confettiSettings = { target: 'my-canvas' , size: 1.8, clock: 15};
  var confetti = new ConfettiGenerator(confettiSettings);
  confetti.render();
};