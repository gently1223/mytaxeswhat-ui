<template>
  <q-layout view="lHh Lpr lFf">
    <q-header :class="$q.dark.isActive ? 'bg-black' : 'bg-primary'">
      <q-toolbar>
        <q-toolbar-title> My Taxes What? </q-toolbar-title>
        <q-btn v-if="$q.dark.isActive" flat round dense @click="toggleDarkMode"
          ><q-img
            src="../assets/dark.svg"
            spinner-color="white"
            style="height: 24px; max-width: 24px"
            class="rounded-borders"
        /></q-btn>
        <q-btn class="grey-9" v-else flat round dense @click="toggleDarkMode"
          ><q-img
            src="../assets/light.svg"
            spinner-color="white"
            style="height: 24px; max-width: 24px"
            class="rounded-borders"
        /></q-btn>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { useQuasar } from "quasar";
import { defineComponent, ref } from "vue";

const linksList = [
  {
    title: "United States Map",
    caption: "Drill Down Map",
    icon: "map",
    link: "/#/map",
  },
];

export default defineComponent({
  name: "MainLayout",

  setup() {
    const $q = useQuasar();

    const toggleDarkMode = () => {
      $q.dark.toggle();
    };
    return {
      toggleDarkMode,
    };
  },
});
</script>
