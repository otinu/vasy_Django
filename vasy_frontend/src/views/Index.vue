<template>
  <div class="d-none d-md-block">
    <bar-menu></bar-menu>
  </div>
  <div class="d-md-none">
    <humberger-menu></humberger-menu>
  </div>
  <div class="container">
    <div class="row">
      <h3 class="col-4 d-none d-lg-block">🍅トマト🍅</h3>
    </div>
    <div class="row g-2">
      <template v-for="data in tomato_datas" :key="data">
        <template v-if="data.count < 3">
          <div class="col-md-4 col-sm-12">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                :src="data.image"
                width="200"
                height="296"
                alt="レシピ画像"
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
      </template>
    </div>

<div class="row">
      <h3 class="col-4 mt-5 d-none d-lg-block">🍆茄子🍆</h3>
    </div>
    <div class="row g-2">
      <template v-for="data in japanese_nasu_datas" :key="data">
        <template v-if="data.count < 3">
          <div class="col-md-4 col-sm-12">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                :src="data.image"
                width="200"
                height="296"
                alt="レシピ画像"
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
      </template>
    </div>


    <div class="row">
      <h3 class="col-4 mt-5 d-none d-lg-block">🥔じゃがいも🥔</h3>
    </div>
    <div class="row g-2">
      <template v-for="data in potato_datas" :key="data">
        <template v-if="data.count < 3">
          <div class="col-md-4 col-sm-12">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                :src="data.image"
                width="200"
                height="296"
                alt="レシピ画像"
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
      </template>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "IndexPage",
  data: () => ({
    open: false,
    potato_datas: [],
    tomato_datas: [],
    japanese_nasu_datas: []
  }),
  mounted() {
    axios
      .get("/products/kurashiru/")
      //.then((response) => (this.message = response.data))
      .then((response) => {
        this.potato_datas = response.data[0];
        this.tomato_datas = response.data[1];
        this.japanese_nasu_datas = response.data[2];
      })
      .catch((error) => console.log(error));
  },
};
</script>
