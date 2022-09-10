<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>



      <div v-for="data in datas" :key="data">

         <img
              :src="data.image"
              alt="レシピ画像"
            />
            <!-- タイトルの長さによって、レイアウトが崩されている -->
          <a
            class="recipe-title text-success"
            id="recipe_title_7294659"
            style="text-decoration: none"
            target="_blank"
            rel="noopener noreferrer"
            :href="data.link"
            >{{data.title}}</a
          >
      </div>

</template>

<script>
import axios from "axios";

export default {
  name: "AxiosTestPage",
  data() {
    return {
      message: "Hay axios",
      datas: []
    };
  },
  mounted() {
    axios
      .get("/products/non_model/")
      //.then((response) => (this.message = response.data))
      .then((response) => {
        this.datas = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>
