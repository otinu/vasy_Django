<template>
  <humberger-menu></humberger-menu>
  <div class="slide__wrapper">
    <div v-show="index === page" v-for="(image, index) in images" :key="index">
      <img :src="image.src" class="image" />
    </div>
    <div class="right-btn" @click="nextPage">＞</div>
    <div class="left-btn" @click="nextPage">＜</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      page: 0,
      images: [
        {
          src: require("@/assets/logo.png"),
        },
        {
          src: require("@/assets/logo2.png"),
        },
        {
          src: require("@/assets/logo.png"),
        },
      ],
    };
  },
  methods: {
    nextPage() {
      if (this.page + 1 >= this.images.length) {
        this.page = 0;
        return;
      }
      this.page++;
    },
    prevPage() {
      if (this.page <= 0) {
        return;
      }
      this.page--;
    },
  },
};
</script>

<style>
.slide__wrapper {
  position: relative;
  width: 40%;
  margin: 0 auto;
}
.image {
  width: 100%;
}
.right-btn {
  position: absolute;
  left: 50vw;
  top: 41%;
  font-size: 50px;
  font-weight: bold;
  color: black;
  border-radius: 30px;
  background-color: aqua;
}
.left-btn {
  position: absolute;
  right: 50vw;
  top: 41%;
  font-size: 25px;
  font-size: 50px;
  font-weight: bold;
  color: black;
  border-radius: 30px;
  background-color: aqua;
}
</style>