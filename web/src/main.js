import Vue from 'vue'
import App from './App.vue'

export const eventBus = new Vue({
    methods: {
        addDownload(download) {
            this.$emit('addDownload', download);
        }
    }
});

new Vue({
  el: '#app',
  render: h => h(App)
});
