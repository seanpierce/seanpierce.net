<template>
    <div class="work">
        <div class="work-title-wrapper">
            <div class="work-title" v-html="title"></div>
            <span class="work-year">{{ work.year }}</span>
        </div>
        <div v-if="images">
            <img v-for="(image, index) in images" 
                class="work-image"
                @click="open(mediaUrl + image)"
                :key="index" 
                :src="mediaUrl + image">
        </div>
        <div v-html="work.content" class="work-content"></div>
    </div>
</template>

<script>
import Vue from 'vue'

export default {
    props: {
        work: {
            type: Object
        }
    },

    data() {
        return {
            test: true
        }
    },

    computed: {
        title() {
            return Vue.filter('formatFont')(this.work.title);
        },
        images() {
            return this.work.images ? this.work.images.split(',') : []
        },
        mediaUrl() {
            return process.env.VUE_APP_MEDIA_URL
        }
    },

    methods: {
        open(url) {
            window.open(url, '_blank')
        }
    }
}
</script>