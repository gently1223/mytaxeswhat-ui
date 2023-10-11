<template>
  <div id="mapContainer"></div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-tilelayer-geojson";

export default {
  name: "MapComponent",
  data() {
    return {
      map: null,
      openTooltip: null,
    };
  },
  mounted() {
    let geojsonLayer;
    this.map = L.map("mapContainer").setView([37.8, -96], 5);
    L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map);

    // Add a click event listener to the map
    this.map.on("click", this.handleMapClick);

    // Load GeoJSON data for the 48 contiguous states
    fetch("us-states.json")
      .then((response) => response.json())
      .then((geojsonData) => {
        // Create a GeoJSON layer and add it to the map
        geojsonLayer = L.geoJSON(geojsonData, {
          style: {
            fillColor: "blue",
            fillOpacity: 0.5,
            color: "white",
            weight: 1,
          },
          onEachFeature: (feature, layer) => {
            layer.on("click", () => {
              geojsonLayer.resetStyle();
              layer.setStyle({ fillColor: "red" });
            });
            layer.on("mouseover", (event) => {
              if (this.openTooltip) {
                this.map.closeTooltip(this.openTooltip);
              }

              this.showTooltip(event);
            });

            layer.on("mouseout", this.hideTooltip);
          },
        }).addTo(this.map);
      })
      .catch((error) => {
        console.error("Error loading GeoJSON data:", error);
      });

    // TODO: mock out backend calls that would retrieve some dummy data about the selected state

    // // Add a click event listener to the map
    // this.map.on("click", this.handleMapClick);
  },
  onBeforeUnmount() {
    if (this.map) {
      this.map.remove();
    }
  },
  methods: {
    showTooltip(event) {
      const layer = event.target;
      const tooltipContent = layer.feature.properties.NAME;

      const tooltip = L.tooltip({
        className: "map-tooltip",
      }).setContent(tooltipContent);

      // Show the tooltip at the mouse pointer's position
      tooltip.setLatLng(event.latlng).openOn(this.map);

      this.openTooltip = tooltip;
    },

    hideTooltip() {
      if (this.openTooltip) {
        this.map.closeTooltip(this.openTooltip);
        this.openTooltip = null;
      }
    },
    handleMapClick(event) {
      // TODO: mock out backend calls that would retrieve some dummy data about the selected state

      const { lat, lng } = event.latlng;
      // You can now fetch additional data or load new map layers based on the click coordinates
      // Example: Fetch data or load a new layer for the clicked location
      // You can use Vue methods or Vuex to manage data and state
    },
  },
};
</script>

<style scoped>
#mapContainer {
  width: 100%;
  height: calc(100vh - 50px);
}
/* CSS class for custom tooltips */
.map-tooltip {
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  border: 1px solid #333;
  padding: 5px;
  border-radius: 3px;
}
</style>
