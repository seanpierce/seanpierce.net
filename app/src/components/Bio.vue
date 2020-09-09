<template>
    <div id="bio" class="hel-out" v-html="content"></div>
</template>

<script>
import Vue from 'vue'

export default {
    data() {
        return {
            bio: 'Sean Pierce is an artist and musician working in Portland, OR. Pierce has released music on labels based in London, Berlin, Glasgow, Chicago, Los Angeles, and Seattle, and he has performed in many cities across North America and Europe.'
        }
    },
    computed: {
        content() {
            try {
                let content = this.bio
                return Vue.filter('formatFont')(content);
            } catch {
                return null
            }
        }
    },
}
</script>