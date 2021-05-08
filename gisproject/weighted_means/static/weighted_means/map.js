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
    L.geoJson(data).addTo(map);
  });

fetch("http://localhost:8000/2011")
  .then((res) => res.json())
  .then((data) => {
    L.geoJson(data).addTo(map);
  });

// https://leaflet-extras.github.io/leaflet-providers/preview/
