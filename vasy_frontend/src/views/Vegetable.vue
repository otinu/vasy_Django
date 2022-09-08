<template>
  <div class="d-none d-md-block">
    <bar-menu></bar-menu>
  </div>
  <div class="d-md-none">
    <humberger-menu></humberger-menu>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-lg-6">
        <h3><i class="fa-solid fa-magnifying-glass"></i>野菜ジャンル名</h3>
        <div v-ripple="'rgba(34, 139, 34, 0.2)'">
          <img
            :src="first_data.image"
            alt="レシピ画像"
            class="img-fluid img-thumbnail w-75 h-100"
          />
        </div>
      </div>
      <div class="col-lg-6 mt-5">
        <div class="row">
          <template v-for="data in second_datas" :key="data">
            <div class="col-sm-6">
              <div v-ripple="'rgba(34, 139, 34, 0.2)'">
                <img
                  :src="data.image"
                  width="200"
                  height="296"
                  alt="レシピ画像"
                  class="img-fluid img-thumbnail"
                />
              </div>
              <a
                class="recipe-title text-success"
                style="text-decoration: none"
                target="_blank"
                rel="noopener noreferrer"
                :href="data.link"
                >{{ data.title }}</a
              >
            </div>
          </template>
        </div>
      </div>

      <div class="col-lg-6 mt-5">
        <div class="row">
          <template v-for="data in third_datas" :key="data">
            <div class="col-sm-6 mt-3">
              <div v-ripple="'rgba(34, 139, 34, 0.2)'">
                <img
                  :src="data.image"
                  width="200"
                  height="296"
                  alt="レシピ画像"
                  class="img-fluid img-thumbnail"
                />
              </div>
              <a
                class="recipe-title text-success"
                style="text-decoration: none"
                target="_blank"
                rel="noopener noreferrer"
                :href="data.link"
                >{{ data.title }}</a
              >
            </div>
          </template>
        </div>
      </div>
      <div class="col-lg-6 mt-5">
        <div v-ripple="'rgba(34, 139, 34, 0.2)'">
          <img
            :src="first_data.image"
            alt="レシピ画像"
            class="img-fluid img-thumbnail w-75 h-100"
          />
        </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "VegetablePage",
  data: () => ({
    first_data: {},
    second_datas: {},
    third_datas: {},
  }),
  mounted() {
    /*
    axios
      .get("/products/kurashiru/", {
        params: {
          limit: 2,
        },
      })
      .then((response) => {
        this.second_datas = response.data;
      })
      .catch((error) => console.log(error));
  },
  */
    axios
      .get("/products/kurashiru/")
      .then((response) => {
        for (var data in response.data) {
          if (data == 0) {
            this.first_data = response.data[data];
          } else if (data < 5) {
            this.second_datas[data] = response.data[data];
          } else if (data < 9) {
            this.third_datas[data] = response.data[data];
          }
        }
      })
      .catch((error) => console.log(error));
  },
};
</script>
