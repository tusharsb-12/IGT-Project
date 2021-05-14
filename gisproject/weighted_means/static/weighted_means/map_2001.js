this.map = L.map("map", {
  center: [22.5, 78.0], // india coordinates
  zoom: 5,
  zoomControl: true,
  trackResize: true,
});

fetch(
  "https://opendata.arcgis.com/datasets/ba24c0b6ade04b43aa1ca8dee504ee7e_0.geojson"
)
  .then((res) => res.json())
  .then((data) => {
    // console.log(data);
    L.geoJson(data).addTo(map);
  });

const tiles = L.tileLayer(
  "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
  {
    attribution: "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
    maxZoom: 16,
  }
);

tiles.addTo(this.map);

fetch("http://localhost:8000/2001")
  .then((res) => res.json())
  .then((data) => {
    L.geoJson(data, {
      pointToLayer: (feature, latlng) => {
        let redIcon = L.icon({
          iconSize: [27, 27],
          iconAnchor: [13, 27],
          popupAnchor: [1, -24],
          iconUrl: "https://img.icons8.com/metro/26/fa314a/circled-dot.png",
        });
        return L.marker(latlng, { icon: redIcon });
      },
    })
      .bindPopup(function (layer) {
        let output = `<strong>State</strong>: ${layer.feature.properties.state}<br /><strong>Coordinates</strong>: ${layer.feature.geometry.coordinates}`;
        return output;
      })
      .openPopup()
      .addTo(map);
  });

var legend = L.control({ position: "topright" });

legend.onAdd = function (map) {
  var div = L.DomUtil.create("div", "legend");
  div.innerHTML += "<h4><strong>Legend</strong></h4>";
  div.innerHTML +=
    '<i style="background: rgb(255, 0, 0)"></i><span>2001</span><br>';
  return div;
};

legend.addTo(map);

// https://leaflet-extras.github.io/leaflet-providers/preview/
