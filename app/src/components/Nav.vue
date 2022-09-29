<template>
    <div id="nav">
        <img id="sean" :src="require('@/assets/images/big-sean.png')" @click="toggleNav()">

        <div id="nav-container">
            <img id="speech" :src="require('@/assets/images/seanpierce-net-speech-bubble.png')">
            <img id="nav-bio" 
                class="nav-item" 
                :src="require('@/assets/images/seanpierce-net-link-bio.png')"
                @click="goTo('/')">
            <img id="nav-works" 
                class="nav-item" 
                :src="require('@/assets/images/seanpierce-net-link-works.png')"
                @click="goTo('/works')">
            <img id="nav-contact" 
                class="nav-item" 
                :src="require('@/assets/images/seanpierce-net-link-contact.png')"
                @click="goTo('contact')">
        </div>

        <img id="bio-background" :src="require('@/assets/images/seanpierce-net-bio.png')">
    </div>
</template>

<script>
export default {
    methods: {
        goTo(path) {
            if (this.$router.history.current.path === path)
                return
                
            this.$router.push(path)
        }
    },
}
</script>