<template>
    <div id="contact" v-html="content">
    </div>
</template>

<script>
import Vue from 'vue'

export default {
    computed: {
        content() {
            try {
                let content = this.$store.state.pages.contact
                return Vue.filter('formatFont')(content);
            } catch {
                return null
            }
        }
    }
}
</script>