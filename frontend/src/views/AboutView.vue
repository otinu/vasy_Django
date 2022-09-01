<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>

  <div id="axios-test">
    <h3>{{ message }}</h3>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AxiosTestPage",
  el: "#axios-test",
  data() {
    return {
      message: "Hay axios",
    };
  },
  mounted() {
    axios
      .get("/products/non_model/")
      .then((response) => (this.message = response.data))
      //.then((response) => console.log(response))
      .catch((error) => console.log(error));
  },
};
</script>
