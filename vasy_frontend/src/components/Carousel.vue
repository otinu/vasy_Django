<template>
  <Carousel>
    <template #slides="{ slidesCount }">
      <Slide v-for="(image, index) in images" :key="image.id">
        <img :src="image.url" />
        <button v-if="slidesCount > 1" @click="deleteImage(index)">x</button>
      </Slide>
    </template>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>

<script src="https://cdn.jsdelivr.net/npm/vue-carousel@0.18.0/dist/vue-carousel.min.js"></script>
<script>
import { defineComponent, registerRuntimeCompiler, toRefs } from "vue";
import { Carousel, Slide, Pagination, Navigation } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "Basic",
  props: {
    images: Array,
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },

  setup(props, { emit }) {
    const { images } = toRefs(props);

    const deleteImage = (index) => emit("delete-image", index);

    return { images, deleteImage };
  },
});
</script>
