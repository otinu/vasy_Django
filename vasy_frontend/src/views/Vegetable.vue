<template>
  <div class="d-none d-md-block">
    <bar-menu></bar-menu>
  </div>
  <div class="d-md-none">
    <humberger-menu></humberger-menu>
  </div>
  <img class="rounded-circle kurashiru-logo mt-5" alt="Kurashiru logo" src="@/assets/kurashiru.png">
  <div class="container" v-cloak>
    <div class="row">
      <div class="col-lg-6">
        <div v-ripple="'rgba(34, 139, 34, 0.2)'">
          <img
            :src="first_big.image"
            alt="レシピ画像"
            class="img-fluid img-thumbnail w-75 h-100 mt-5"
          />
        </div>
        <h4><a
                  class="recipe-title text-success"
                  style="text-decoration: none"
                  target="_blank"
                  rel="noopener noreferrer"
                  :href="first_big.link"
                  >{{ first_big.title }}</a
                ></h4>
      </div>
      <div class="col-lg-6 mt-5">
        <div class="row">
          <template v-for="data in first_datas" :key="data">
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
          <template v-for="data in second_datas" :key="data">
            <template v-if="data.count < 10">
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
          </template>
        </div>
      </div>
      <div class="col-lg-6 mt-5">
        <div v-ripple="'rgba(34, 139, 34, 0.2)'">
          <img
            :src="second_big.image"
            alt="レシピ画像"
            class="img-fluid img-thumbnail w-75 h-100"
          />
        </div>
        <h4><a
                  class="recipe-title text-success"
                  style="text-decoration: none"
                  target="_blank"
                  rel="noopener noreferrer"
                  :href="second_big.link"
                  >{{ second_big.title }}</a
                ></h4>
      </div>

</div>

      <img class="rounded-circle cookpad-logo w-25 h-25 mt-5" alt="Cookpad logo" src="@/assets/cookpad.png">


<div class="row">
      <template v-for="data in cookpad_datas" :key="data">
        <template v-if="data.count < 10">
          <div class="col-sm-4 mt-3">
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
      </template>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "VegetablePage",
  data: () => ({
    first_big: {},
    first_datas: {},
    second_big: {},
    second_datas: {},
    third_big: {},
    third_datas: {},
    fourth_big: {},
    fourth_datas: {},
    cookpad_datas: {},
  }),
  mounted() {
    axios
      .get("/products/kurashiru/")
      .then((response) => {
        for (var data in response.data[0]) {
          if (data == 0) {
            this.first_big = response.data[0][data];
          } else if (data < 5) {
            this.first_datas[data] = response.data[0][data];
          } else if (data == 5) {
            this.second_big = response.data[0][data];
          } else {
            this.second_datas[data] = response.data[0][data];
          }
        }
      })
      .catch((error) => console.log(error));
    axios
      .get("/products/cookpad/")
      .then((response) => {
        this.cookpad_datas = response.data[0];
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style>
.kurashiru-logo {
  width: 23%;
  height: 23%;
}
</style>