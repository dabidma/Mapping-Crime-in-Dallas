// Creating our initial map object:
// We set the longitude, latitude, and starting zoom level.
// This gets inserted into the div with an id of "map".
let myMap = L.map("map", {
    center: [32.799, -96.797],
    zoom: 10
  
  });
  
  // Adding a tile layer (the background map image) to our map:
  // We use the addTo() method to add objects to our map.
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
//---------------------
//this add marker for every crime 
for (i=0; i<month_data.length;i++) {
  let item = month_data[i]
  console.log([item.lat, item.lon])
  let marker = L.marker([item.lat, item.lon], {
    draggable: false,
    title: "My First Marker"
  }).bindPopup(`${item.arladdress} <br> Arrest Time: ${item.ararrestdate}`).openPopup().addTo(myMap)
};


// attempt at heatmap
console.log(month_data)
// let heatArray = [];

// for (let i = 0; i < month_data.length; i++) {
//   let location = month_data[i];
//     console.log([[location.lat, location.lon]])
//     heatArray.push([location.lat, location.lon]);
// }

// // console.log(heatArray)
// let heat = L.heatLayer(heatArray, {
//   radius: 20,
//   blur: 35
// }).addTo(myMap);


//-------------------------

let monthly_drugs = month_data.map(data => data.drugtype).filter(data => data != null)
let drugs=['Marijuana', 'Cocaine', 'Methamphetamine','Heroin','Hydrocone','Ectasy','Oxycodone', 'GHB', 'Ketamine','Other Prescription Drugs','Other Non-Prescription Drugs']
// console.log(monthly_drugs)
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
for (let i=0; i<month_data.length; i++) {
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
    type: 'bar',
    marker:{color: 'rgb(142,124,195)'}
  };
  
  let data = [trace1];
  
  let layout = {
    title: "Popular Drugs During Arrests",
    width: 700,
    height: 500,
    font:{
      family: 'Roboto, monospace'
    },
    xaxis: {
      title: {
        text: 'Drug Name',
        font: {
          family: 'Roboto, monospace',
          size: 25
        }
      },
    }, 
    yaxis: {
      title: {
        text: 'Number of Arrests',
        font: {
          family: 'Roboto, monospace',
          size: 25
        }
      },
    },
  };
  
  Plotly.newPlot("chart1", data, layout);






