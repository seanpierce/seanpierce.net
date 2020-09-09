<template>
    <div id="work">
        <h1 v-html="formatContent(work.title)"></h1>
        <div id="content"
            v-html="work.content">
        </div>
        <router-link to="/works" class="back">&lt;</router-link>
    </div>
</template>

<script>
export default {
    props: {
        slug: String
    },
    methods: {
        formatContent(input) {
            let stringArray = input.split('')
            stringArray.forEach((character, index) => {
                if (character.toLowerCase() === 's' || character.toLowerCase() === 'p')
                    stringArray[index] = `<span class="yolda">${character}</span>`
            });
            return stringArray.join('')
        }
    },
    computed: {
        work() {
            return this.$store.getters.getWorkBySlug(this.slug)
        }
    }
}
</script>