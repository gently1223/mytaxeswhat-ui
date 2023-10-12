<template>
  <div id="mapContainer">
    <!-- Map container element -->
  </div>
  <q-dialog v-model="dataFetched">
    <q-card style="width: 700px; max-width: 80vw">
      <q-card-section class="q-pt-none">
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>Nickame</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.nickname }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>Statehood</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.statehood }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>Population</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.population }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>Capital</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.capital }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>Biggest City</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.biggestcity }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>State bird</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.statebird }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>State flower</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ this.dummyData.stateflower }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
      </q-card-section>

      <q-card-actions align="right" class="bg-white text-teal">
        <q-btn flat label="OK" v-close-popup></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-tilelayer-geojson";
import api from "../services/api";

export default {
  name: "MapComponent",
  data() {
    return {
      map: null,
      selectedState: null,
      dataFetched: false,
      dummyData: null,
    };
  },
  mounted() {
    let geojsonLayer;
    this.map = L.map("mapContainer", {}).setView([37.8, -96], 5);
    L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map);

    fetch("us-states.json")
      .then((response) => response.json())
      .then((geojsonData) => {
        geojsonLayer = L.geoJSON(geojsonData, {
          style: {
            fillColor: "blue",
            fillOpacity: 0.5,
            color: "white",
            weight: 1,
          },
          onEachFeature: (feature, layer) => {
            layer.on("click", async () => {
              geojsonLayer.resetStyle();
              layer.setStyle({ fillColor: "red" });

              this.dataFetched = false;
              this.dummyData = null;

              try {
                const response = await api.fetchData(
                  this.selectedState._content
                );
                this.dummyData = response.data;
                console.log("State Information: ", this.dummyData.nickname);
                this.dataFetched = true;
              } catch (error) {
                console.error(error);
              }
            });
            layer.on("mouseover", (event) => {
              if (this.selectedState) {
                this.map.closeTooltip(this.selectedState);
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
  },
  onBeforeUnmount() {
    if (this.map) {
      this.map.remove();
    }
  },
  methods: {
    showTooltip(event) {
      const layer = event.target;
      const tooltipContent = layer.feature.properties.name;

      if (this.selectedState) {
        this.hideTooltip();
      }

      this.selectedState = L.tooltip({
        className: "map-tooltip",
      })
        .setContent(tooltipContent)
        .setLatLng(event.latlng)
        .openOn(this.map);
    },

    hideTooltip() {
      if (this.selectedState) {
        this.map.closeTooltip(this.selectedState);
        this.selectedState = null;
      }
    },
  },
};
</script>

<style scoped>
#mapContainer {
  width: 100%;
  height: calc(100vh - 50px);
}
.map-tooltip {
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  border: 1px solid #333;
  padding: 5px;
  border-radius: 3px;
}
</style>
