<template>
<div id="app">
  <humberger-menu></humberger-menu>
  <ScreenTransitionLoading :active="isLoading" @click.prevent="loadingCancel()" />
  <form
    id="login-form"
    @submit.prevent="submit"
    class="vld-parent"
    ref="formContainer"
  >
    <!-- your form inputs goes here -->
    <label><input type="checkbox" v-model="fullPage" />Full page?</label>
    <button type="submit">Login</button>
  </form>

</div>
</template>


<script>

export default {
  data() {
    return {
      fullPage: false,
      isLoading: true
    };
  },
  methods: {
    submit() {
      let loader = this.$loading.show({
        // Optional parameters
        loader: 'bars', // spinner\dots
        color: "red",
        container: this.fullPage ? null : this.$refs.formContainer,
        canCancel: true,
        onCancel: this.onCancel
      });
      // simulate AJAX
      setTimeout(() => {
        loader.hide();
      }, 5000);
    },
    onCancel() {
      console.log("User cancelled the loader.");
    },
    loadingCancel() {
      this.isLoading = false
    }
  }
};
</script>

<style>
#login-form {
  background: #f8f8f8;
  min-height: 400px;
  border: 2px solid #000;
}
</style>