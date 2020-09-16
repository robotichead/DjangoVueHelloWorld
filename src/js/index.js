//import Vue from 'vue';
import Vue from 'vue/dist/vue.js';

//Vue Component Library
import HelloWorld from "./Components/HelloWorld.vue";

//Global NearBeach Vue Components
Vue.component('HelloWorld',HelloWorld);

window.vm = new Vue({
    el: "#app",
    components: {},
    data() {
        return {};
    },
    methods: {},
    mounted() {
        //TELL USER VUE HAS LOADED
        console.log("Vue has loaded");
    }
});