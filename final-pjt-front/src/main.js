import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VModal from 'vue-js-modal'
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify'
import Paginate from 'vuejs-paginate'


Vue.config.productionTip = false
Vue.use(VModal, VueGlide, { dynamic:true })
Vue.use(BootstrapVue)
Vue.component('paginate', Paginate)

new Vue({
  el: '#app',
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

var filter = function(text, length, clamp){
  clamp = clamp || '...';
  var node = document.createElement('div');
  node.innerHTML = text;
  var content = node.textContent;
  return content.length > length ? content.slice(0, length) + clamp : content;
};

Vue.filter('truncate', filter);
