<template>
    <div id="menu">
        <h1>FLORESCENT</h1>
        <img :src="require('@/assets/cherub.png')" 
            @click="toggleMenu()"
            id="menu-cherub"
            alt="Florescent cherub">
        <div id="menu-modal" v-bind:class="{ 'show-menu': showMenu }">
            <ul>
                <li>
                    <router-link to="/gallery">GALLERY</router-link>
                </li>
                <li>
                    <router-link to="/shop">SHOP</router-link>
                </li>
                <li>
                    <router-link to="/contact">CONTACT</router-link>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showMenu: false
        }
    },
    watch: {
        $route(){
            this.showMenu = false;
        }
    },
    methods: {
        toggleMenu() {
            this.showMenu = !this.showMenu;
        }
    }
}
</script>