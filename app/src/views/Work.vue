<template>
    <div id="work" v-if="work">
        <h1 v-html="title"></h1>
        <div id="content"
            v-html="work.content">
        </div>
        <div id="images" v-if="images">
            <img v-for="(image, index) in images" 
                :key="index" 
                :src="mediaUrl + image">
        </div>
        <router-link to="/works" class="back">&lt;</router-link>
    </div>
</template>

<script>
import Vue from 'vue'

export default {
    data() {
        return {
            mediaUrl: process.env.VUE_APP_MEDIA_URL
        }
    },
    props: {
        slug: String
    },
    computed: {
        title() {
            try {
                let content = this.work.title
                return Vue.filter('formatFont')(content);
            } catch {
                return null
            }
        },
        work() {
            return this.$store.getters.getWorkBySlug(this.slug)
        },
        images() {
            try {
                return this.work?.images.split(',')
            } catch {
                return null
            }
        }
    }
}
</script>