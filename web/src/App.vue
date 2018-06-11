<template>
  <div id="app">
    <navbar></navbar>
  </div>
</template>

<script>
import Navbar from './navbar.vue';

export default {
  name: 'app',
  components: {
    navbar: Navbar
  }
}
</script>

<style lang="scss">
body {
  margin: 0px;
  background-color: #1c1c1c;
}

@font-face {
  font-family: "NotoSans";
  src: url("assets/NotoSans-Bold.ttf");
  font-weight: bold;
}

@font-face {
  font-family: "NotoSansCondensed";
  src: url("assets/NotoSans-ExtraCondensedBold.ttf");
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
