<template>
    <div id="nav">
        <img id="sean" :src="require('@/assets/images/big-sean.png')" @click="toggleNav()">
        <div id="nav-modal" v-bind:class="{ showNav: showNav }">
            <ul class="hel-out">
                <li>
                    <router-link @click="test()" to="/">Bio</router-link>
                </li>
                <li>
                    <router-link to="/works">Works</router-link>
                </li>
                <li>
                    <router-link to="/contact">Contact</router-link>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showNav: false
        }
    },
    methods: {
        toggleNav() {
            this.showNav = !this.showNav
        }
    },
    watch:{
        $route() {
            this.showNav = false;
        }
    } 
}
</script>