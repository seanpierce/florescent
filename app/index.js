import App from './components/App.vue';

export const app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    components: {
        'App': App
    },
    data: {
        loaded: false,
    },
    methods: {
    },
    computed: {
        route() {
            switch(window.location.pathname) {
                case '/':
                    return 'home';
                case '/gallery':
                    return 'gallery';
            }
        }
    },
    mounted() {
        this.loaded = true;
    },
    template: `
        <App />
    `
  })