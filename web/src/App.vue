<template>
    <div id="app">
        <navbar></navbar>
        <download-form></download-form>
    </div>
</template>

<script>
import Navbar from './navbar.vue';
import DownloadForm from './download_form.vue';

export default {
  name: 'app',
  components: {
    navbar: Navbar,
    downloadForm: DownloadForm
  }
}
</script>

<style lang="scss">
html {
    height: 100%;
}
body {
  margin: 0px;
  background-color: #121212;
  height: 100%;
}

@font-face {
  font-family: "NotoSans";
  src: url("assets/NotoSans-Bold.ttf");
  font-weight: bold;
}

@font-face {
  font-family: "NotoSans";
  src: url("assets/NotoSans-Regular.ttf");
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
  height: 100%;

  font-family: "NotoSans";
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
