<template>
  <div class="mb-4">
      <router-link to="/" class="menu__item link-dark h5" >Index</router-link>
      <router-link to="/vegetable" class="menu__item link-dark h5" >Vegetable</router-link>
      <router-link to="/recipe" class="menu__item link-dark h5" >Recipe</router-link>
      <router-link to="/carousel" class="menu__item link-dark h5" >Carousel</router-link>
      <router-link to="/loading" class="menu__item link-dark h5" >TestLoading</router-link>
  </div>
</template>

<script>

export default {
  name: 'HumbergerMenu'
}
</script>
