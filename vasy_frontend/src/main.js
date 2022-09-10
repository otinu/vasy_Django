// このファイルが全ファイル共通になるJSファイル

import { createApp} from 'vue'
import App from './App.vue'
import Menu from "@/components/BarMenu.vue"
import HumbergerMenu from "@/components/HumbergerMenu.vue"
import router from './router'
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
import Ripple from 'vue3-whr-ripple-directive'

const app = createApp(App)
app.use(router)
app.component('bar-menu', Menu)
app.component('humberger-menu', HumbergerMenu)
app.component("ScreenTransitionLoading", Loading)
app.use(Loading) // ボタン押下時のローディング
app.directive('ripple', Ripple) // 「v-ripple」というカスタムディレクティブを設定

app.mount('#app')