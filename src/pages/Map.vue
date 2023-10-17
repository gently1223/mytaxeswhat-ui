<template>
  <div id="desktopMap">
    <!-- Desktop Map container element -->
  </div>
  <div id="mobileMap">
    <!-- Mobile Map container element -->
  </div>
  <q-drawer
    side="right"
    v-model="dataFetched"
    bordered
    :width="300"
    :breakpoint="500"
    :class="darkModeClass"
  >
    <q-scroll-area class="fit">
      <div class="q-pa-sm">
        <q-list v-if="dummyData">
          <q-item>
            <q-item-section>
              <q-item-label>Nickname</q-item-label>
            </q-item-section>

            <q-item-section side>
              <q-item-label>{{ dummyData.nickname }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator />
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
        <q-separator />
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
        <q-separator />
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
        <q-separator />
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
        <q-separator />
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
        <q-separator />
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
      </div>
    </q-scroll-area>
  </q-drawer>
</template>

<script>
import { ref, computed, watchEffect, onMounted, onBeforeUnmount } from "vue";
import { useQuasar } from "quasar";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import "leaflet-tilelayer-geojson";
import api from "../services/api";

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
      fetch("us-states.json")
        .then((response) => response.json())
        .then((geojsonData) => {
          geojsonLayer.value = L.geoJSON(geojsonData, {
            style: {
              fillColor: "blue",
              fillOpacity: 0.5,
              color: "white",
              weight: 1,
            },
            onEachFeature: (feature, layer) => {
              let tooltip;
              layer.on("click", async () => {
                geojsonLayer.value.resetStyle();
                layer.setStyle({ fillColor: "red" });
                dataFetched.value = false;
                dummyData.value = null;
                try {
                  const stateInfo = feature.properties;
                  console.log("Selected State Information: ", stateInfo.name);
                  selectedState.value = stateInfo.name;
                  const response = await api.fetchData(stateInfo.name);
                  dummyData.value = response.data;
                  console.log("State Information: ", dummyData.value.nickname);
                  dataFetched.value = true;
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
      // if (map.value) {
      //   map.value.remove();
      // }
    });

    return {
      isDesktop,
      isMobile,
      dataFetched,
      dummyData,
      darkModeClass,
      selectedState,
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
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
.map-tooltip {
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  border: 1px solid #333;
  padding: 5px;
  border-radius: 3px;
}
</style>
