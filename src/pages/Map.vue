<template>
  <div class="container">
    <div id="interactingMap"></div>
    <div id="desktopMap"></div>
    <div id="mobileMap"></div>
  </div>

  <q-dialog
    v-model="dataFetched"
    :transition-duration="0"
    fullscreen
    @hide="onDialogClose"
  >
    <q-card>
      <q-card-section>
        <div class="text-h6">{{ this.dummyData.name }}</div>
      </q-card-section>

      <q-separator />

      <q-card-section>
        <q-scroll-area style="height: 50vh; width: 360px">
          <q-list v-if="dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>Nickname</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.nickname }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-list v-if="this.dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>Statehood</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.statehood }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-list v-if="this.dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>Population</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.population }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-list v-if="this.dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>Capital</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.capital }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-list v-if="this.dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>Biggest City</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.biggestcity }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-list v-if="this.dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>State bird</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.statebird }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-list v-if="this.dummyData">
            <q-item>
              <q-item-section>
                <q-item-label>State flower</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-item-label>{{ this.dummyData.stateflower }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn flat label="OK" color="primary" v-close-popup />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { ref, computed, watchEffect, onMounted, onBeforeUnmount } from "vue";
import { useQuasar } from "quasar";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-tilelayer-geojson";
import api from "../services/api";
import * as d3 from "d3";
import square from "@turf/square";

export default {
  name: "MapComponent",
  setup() {
    const $q = useQuasar();
    const isDesktop = ref(false);
    const isMobile = ref(false);
    const dataFetched = ref(false);
    const dummyData = ref(null);
    const darkModeClass = computed(() => ({
      "bg-grey-9": $q.dark.isActive,
      "bg-grey-3": !$q.dark.isActive,
    }));

    const selectedState = ref(null);

    const map = ref(null);
    const geojsonLayer = ref(null);

    const onDialogClose = () => {
      const interactingMap = document.getElementById("interactingMap");
      while (interactingMap.firstChild) {
        interactingMap.removeChild(interactingMap.firstChild);
      }
    };
    var config = {
      width: 392,
      height: 400,
      padding: 0,
      projection: d3.geoMercator(),
      duration: 2000,
      key: function (d) {
        return d.properties.short;
      },
      grid: {
        alaska: { x: 0, y: 0 },
        maine: { x: 0, y: 0 },
        vt: { x: 0, y: 0 },
        nh: { x: 0, y: 0 },
        wash: { x: 0, y: 0 },
        idaho: { x: 0, y: 0 },
        mont: { x: 0, y: 0 },
        nd: { x: 0, y: 0 },
        minn: { x: 0, y: 0 },
        ill: { x: 0, y: 0 },
        wis: { x: 0, y: 0 },
        mich: { x: 0, y: 0 },
        ny: { x: 0, y: 0 },
        ri: { x: 0, y: 0 },
        mass: { x: 0, y: 0 },
        ore: { x: 0, y: 0 },
        nev: { x: 0, y: 0 },
        wyo: { x: 0, y: 0 },
        sd: { x: 0, y: 0 },
        iowa: { x: 0, y: 0 },
        ind: { x: 0, y: 0 },
        ohio: { x: 0, y: 0 },
        pa: { x: 0, y: 0 },
        nj: { x: 0, y: 0 },
        conn: { x: 0, y: 0 },
        calif: { x: 0, y: 0 },
        utah: { x: 0, y: 0 },
        colo: { x: 0, y: 0 },
        neb: { x: 0, y: 0 },
        mo: { x: 0, y: 0 },
        ky: { x: 0, y: 0 },
        wva: { x: 0, y: 0 },
        va: { x: 0, y: 0 },
        md: { x: 0, y: 0 },
        del: { x: 0, y: 0 },
        ariz: { x: 0, y: 0 },
        nm: { x: 0, y: 0 },
        kan: { x: 0, y: 0 },
        ark: { x: 0, y: 0 },
        tenn: { x: 0, y: 0 },
        nc: { x: 0, y: 0 },
        sc: { x: 0, y: 0 },
        dc: { x: 0, y: 0 },
        okla: { x: 0, y: 0 },
        la: { x: 0, y: 0 },
        miss: { x: 0, y: 0 },
        ala: { x: 0, y: 0 },
        ga: { x: 0, y: 0 },
        hawaii: { x: 0, y: 0 },
        texas: { x: 0, y: 0 },
        fla: { x: 0, y: 0 },
        pc: { x: 0, y: 0 },
      },
    };

    if ($q.platform.is.mobile) {
      config.width = $q.screen.width - 40;
    }

    onMounted(() => {
      if ($q.platform.is.desktop == true) {
        map.value = L.map("desktopMap", { minZoom: 4 }).setView([37.8, -96], 5);
        isDesktop.value = true;
      } else {
        console.log("This is mobile");
        map.value = L.map("mobileMap").setView([37.8, -96], 3);
        isMobile.value = true;
      }
      L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map.value);
      var southWest = L.latLng(18.396308, -165.0); // Southwest corner of the United States
      var northEast = L.latLng(70.345786, -54.93457); // Northeast corner of the United States
      var bounds = L.latLngBounds(southWest, northEast);
      map.value.setMaxBounds(bounds);
      if ($q.platform.is.desktop == true) {
        map.value.on("zoomend", function () {
          if (map.value.getZoom() < 5) {
            map.value.setView([46.5, -121], 4);
          }
        });
      } else {
        map.value.on("zoomend", function () {
          if (map.value.getZoom() < 4) {
            map.value.setView([46.5, -121], 3);
          }
        });
      }
      const leafletMap = map.value;
      fetch("us.geojson")
        .then((response) => response.json())
        .then((geojsonData) => {
          geojsonLayer.value = L.geoJSON(geojsonData, {
            style: {
              fillColor: "blue",
              fillOpacity: 0.5,
              color: "white",
              weight: 0.3,
            },
            onEachFeature: (feature, layer) => {
              layer.on("click", async () => {
                geojsonLayer.value.resetStyle();
                layer.setStyle({ fillOpacity: 0, color: "red", weight: 3 });
                dataFetched.value = false;
                dummyData.value = null;
                try {
                  const stateInfo = feature.properties;
                  console.log(
                    "Selected State Information: ",
                    stateInfo.STATE_NAME
                  );
                  selectedState.value = stateInfo.STATE_NAME;
                  selectedState.value = selectedState.value.split(" ").join("");
                  console.log("selectedState", selectedState.value);
                  const response = await api.fetchData(selectedState.value);
                  dummyData.value = response.data;
                  console.log("State Information: ", dummyData.value.name);
                  setTimeout(() => {
                    dataFetched.value = true;
                  }, 1800);
                } catch (error) {
                  console.error(error);
                }

                const interactingMap =
                  document.getElementById("interactingMap");
                while (interactingMap.firstChild) {
                  interactingMap.removeChild(interactingMap.firstChild);
                }
                const svg = d3
                  .select("#interactingMap")
                  .append("svg")
                  .style("fill", "none")
                  .style("stroke", "black")
                  .attr("width", config.width)
                  .attr("height", config.height);

                var g2r = new geo2rect.draw();

                const geojsonPath = "us.geojson?timestamp=" + Date.now();
                d3.json(geojsonPath).then(function (data) {
                  function getStateFeatures(stateName) {
                    return data.features.find(
                      (feature) =>
                        feature.properties.STATE_NAME.split(" ")
                          .join("")
                          .toLowerCase() === stateName.toLowerCase()
                    );
                  }

                  console.log("selectedState.value", selectedState.value);
                  const features = getStateFeatures(selectedState.value);

                  console.log("features", features);

                  const transformedData = {
                    type: "FeatureCollection",
                    crs: {
                      type: "name",
                      properties: { name: "urn:ogc:def:crs:OGC:1.3:CRS84" },
                    },
                    features: [
                      {
                        type: "Feature",
                        properties: features.properties,
                        geometry: features.geometry,
                      },
                    ],
                  };
                  console.log("transformedData", transformedData);

                  let b = turf.bbox(features);

                  let geoCoordinate = [
                    (b[2] - b[0]) / 2 + b[0],
                    (b[1] - b[3]) / 2 + b[3],
                  ];

                  var geojson = geo2rect.compute(transformedData);

                  g2r.config = config;
                  g2r.data = geojson;
                  g2r.svg = svg.append("g");
                  g2r.draw();
                  // TO React Type
                  g2r.toggle();
                  g2r.draw();
                  console.log(g2r.mode);
                });
              });
            },
          }).addTo(leafletMap);
        })
        .catch((error) => {
          console.error("Error loading GeoJSON data:", error);
        });
    });

    onBeforeUnmount(() => {
      if (map.value) {
        map.value.remove();
      }
    });

    return {
      isDesktop,
      isMobile,
      dataFetched,
      dummyData,
      darkModeClass,
      selectedState,
      onDialogClose,
    };
  },
};
</script>

<style scoped>
.container {
  position: relative;
  width: 100%;
  height: calc(100vh - 50px);
}
#interactingMap {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
}
#desktopMap {
  width: 100%;
  height: calc(100vh - 50px);
  position: absolute;
}

#mobileMap {
  width: 100%;
  height: calc(400px);
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
</style>
