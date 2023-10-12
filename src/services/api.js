import { statesData } from "../../public/mockData";

export default {
  fetchData: async (selectedState) => {
    selectedState = selectedState.split(" ").join("");

    // Simulate a delay to mimic network latency
    await new Promise((resolve) => setTimeout(resolve, 1000));
    // Mock data retrieval based on the selected state
    if (statesData[selectedState]) {
      console.log(statesData[selectedState]);
      return { data: statesData[selectedState] };
    } else {
      throw new Error(`Data for ${selectedState} not found.`);
    }
  },
};
