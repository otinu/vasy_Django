<template>
  <div class="d-none d-md-block">
    <bar-menu></bar-menu>
  </div>
  <div class="d-md-none">
    <humberger-menu></humberger-menu>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-lg-6 mb-5">
        <h3><i class="fa-solid fa-magnifying-glass"></i>野菜ジャンル名</h3>
        <div v-ripple="'rgba(34, 139, 34, 0.2)'">
          <img
            src="https://img.cpcdn.com/recipes/7294659/200x296c/27651caeb80a0853714ba26bb9b922db?u=4768165&p=1661432365"
            alt="レシピ画像"
            class="img-fluid img-thumbnail w-75 h-100"
          />
        </div>
      </div>
      <div class="col-lg-6">
        <div class="row">
          <div class="col-sm-6">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                src="https://img.cpcdn.com/recipes/7294659/200x296c/27651caeb80a0853714ba26bb9b922db?u=4768165&p=1661432365"
                alt="レシピ画像"
                class="img-fluid img-thumbnail"
              />
            </div>
            <p class="text-success">テキスト</p>
          </div>
          <div class="col-sm-6">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                src="https://img.cpcdn.com/recipes/7294659/200x296c/27651caeb80a0853714ba26bb9b922db?u=4768165&p=1661432365"
                alt="レシピ画像"
                class="img-fluid img-thumbnail"
              />
            </div>
            <p class="text-success">テキスト</p>
          </div>
          <div class="col-sm-6">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                src="https://img.cpcdn.com/recipes/7294659/200x296c/27651caeb80a0853714ba26bb9b922db?u=4768165&p=1661432365"
                alt="レシピ画像"
                class="img-fluid img-thumbnail"
              />
            </div>
            <p class="text-success">テキスト</p>
          </div>
          <div class="col-sm-6">
            <div v-ripple="'rgba(34, 139, 34, 0.2)'">
              <img
                src="https://img.cpcdn.com/recipes/7294659/200x296c/27651caeb80a0853714ba26bb9b922db?u=4768165&p=1661432365"
                alt="レシピ画像"
                class="img-fluid img-thumbnail"
              />
            </div>
            <p class="text-success">テキスト</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "VegetablePage",
};
</script>