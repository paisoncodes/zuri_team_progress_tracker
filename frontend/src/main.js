import { createApp } from 'vue'
import App from './App.vue'
import mitt from 'mitt'
import router from './router'
import store from './store'
import './index.css'

// font awsome
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';

const eventBus = mitt() 
const app = createApp(App)

app.config.globalProperties.eventBus = eventBus
app.use(app).use(store).use(router).mount('#app')

// createApp(App).use(app).use(store).use(router).mount('#app')
