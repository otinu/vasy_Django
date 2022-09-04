<template>
  <humberger-menu></humberger-menu>
  <Carousel :images="images" @deleteImage="handelDeleteImage" />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const _images = [
      { id: 1, url: "https://picsum.photos/300/200?q=1" },
      { id: 2, url: "https://picsum.photos/300/200?q=2" },
      { id: 3, url: "https://picsum.photos/300/200?q=3" },
      { id: 4, url: "https://picsum.photos/300/200?q=4" },
    ];
    const images = ref(_images);
    const handelDeleteImage = (index: number) => images.value.splice(index, 1);

    return { handelDeleteImage, images };
  },
});
</script>