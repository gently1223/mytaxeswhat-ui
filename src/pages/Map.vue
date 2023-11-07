<template>
  <div id="desktopMap" v-if="$q.platform.is.desktop"></div>
  <div id="mobileMap" v-if="$q.platform.is.mobile"></div>
  <path
    id="rectangle"
    d="M479.5 138.5 L869.5 138.5 L869.5 763.5 L479.5 763.5 Z"
  />
  <q-dialog
    v-if="$q.platform.is.mobile"
    v-model="dataFetched"
    :transition-duration="0"
    fullscreen
    maximized
    @hide="onDialogClose"
  >
    <q-card>
      <q-card-section>
        <div v-if="this.dummyData" class="text-h6">
          {{ this.dummyData.name }}
        </div>
      </q-card-section>

      <q-separator />

      <q-card-section>
        <q-scroll-area style="height: 450px; width: 360px">
          <q-list v-if="this.dummyData">
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
  <q-dialog
    v-model="dataFetched"
    :transition-duration="0"
    v-if="$q.platform.is.desktop"
    @hide="onDialogClose"
  >
    <q-card>
      <q-card-section>
        <div v-if="this.dummyData" class="text-h6">
          {{ this.dummyData.name }}
        </div>
      </q-card-section>

      <q-separator />

      <q-card-section>
        <q-scroll-area style="height: 450px; width: 360px">
          <q-list v-if="this.dummyData">
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
import { ref, computed, onMounted, onUnmounted, onBeforeUnmount } from "vue";
import { useQuasar } from "quasar";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-tilelayer-geojson";
import api from "../services/api";
import gsap from "gsap-trial";
import MorphSVGPlugin from "gsap-trial/MorphSVGPlugin";
import { whileStatement } from "@babel/types";
gsap.registerPlugin(MorphSVGPlugin);
gsap.config({ trialWarn: false });

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
    var selectedId;

    const selectedState = ref(null);

    const map = ref(null);
    const geojsonLayer = ref(null);

    const onDialogClose = () => {
      var morph2 = gsap.to(selectedId, {
        duration: 1,
        morphSVG: selectedId,
        paused: true,
      });

      morph2.play();
    };

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
              layer.on("click", async (event) => {
                let ele = event.target.getElement();

                ele.setAttribute("id", feature.properties.short);

                // Calculate the position and size of target svg in screen
                const svg = document.querySelector("svg");
                console.log("svg", svg);
                const transformStyle = window
                  .getComputedStyle(svg)
                  .getPropertyValue("transform");
                console.log("transformstyle", transformStyle);
                const transformValues = transformStyle.match(
                  /matrix\(([^,]+), ([^,]+), ([^,]+), ([^,]+), ([^,]+), ([^)]+)\)/
                );
                let translateX;
                let translateY;
                if (transformValues && transformValues.length === 7) {
                  translateX = parseFloat(transformValues[5]);
                  translateY = parseFloat(transformValues[6]);

                  console.log(
                    `TranslateX: ${translateX}, TranslateY: ${translateY}`
                  );
                } else {
                  console.log(
                    "Matrix values not found or in the expected format."
                  );
                }

                //
                const viewBoxStyle = svg.getAttribute("viewBox");
                console.log("viewBox", viewBoxStyle);
                const viewBoxValues = viewBoxStyle
                  .split(" ")
                  .map((value) => parseInt(value, 10));

                if (viewBoxValues.length === 4) {
                  const value1 = viewBoxValues[0];
                  const value2 = viewBoxValues[1];
                  const value3 = viewBoxValues[2];
                  const value4 = viewBoxValues[3];

                  console.log(`Value 1: ${value1}`);
                  console.log(`Value 2: ${value2}`);
                  console.log(`Value 3: ${value3}`);
                  console.log(`Value 4: ${value4}`);
                } else {
                  console.log("Input string does not contain four values.");
                }

                const diffScreenX = ((2304 - viewBoxValues[2]) / 2304) * 194.5;
                const diffScreenY = ((1141 - viewBoxValues[3]) / 1141) * 106;

                console.log("diffScreenX", diffScreenX);

                const diffX = translateX + 139;
                const diffY = translateY + 86;

                const path = document.getElementById("rectangle");

                const pathWidth = 390;
                const pathHeight = 596;
                if ($q.screen.height <= 648) {
                  pathHeight = $q.screen.height - 48;
                }
                let centerX = ($q.screen.width - pathWidth) / 2 + 53;
                let centerY = ($q.screen.height - pathHeight) / 2 - 40;
                centerX = centerX + diffX - diffScreenX;
                centerY = centerY + diffY - diffScreenY;

                const pathData = `M${centerX} ${centerY} L${
                  centerX + pathWidth
                } ${centerY} L${centerX + pathWidth} ${
                  centerY + pathHeight
                } L${centerX} ${centerY + pathHeight} Z`;
                // TODO: GSAP animation Add
                selectedId = "#" + feature.properties.short;

                var morph1 = gsap.to(selectedId, {
                  duration: 1,
                  morphSVG: {
                    shape: pathData,
                  },
                });

                morph1.play();

                geojsonLayer.value.resetStyle();
                layer.setStyle({
                  fillOpacity: 1,
                  fillColor: "white",
                  color: "black",
                  weight: 1,
                });
                dummyData.value = null;
                try {
                  const stateInfo = feature.properties;
                  selectedState.value = stateInfo.STATE_NAME;
                  selectedState.value = selectedState.value.split(" ").join("");
                  const response = await api.fetchData(selectedState.value);
                  dummyData.value = response.data;
                  setTimeout(() => {
                    dataFetched.value = true;
                  }, 1000);
                } catch (error) {
                  console.error(error);
                }
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
#desktopMap {
  width: 100%;
  height: calc(100vh - 50px);
}

#mobileMap {
  width: 100%;
  height: calc(400px);
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
</style>
