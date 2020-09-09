<template>
    <div id="works">
        <ul>
            <router-link tag="li" 
                v-for="work in works" 
                :key="work.id" 
                v-html="formatContent(work.title)"
                :to="'/works/' + work.slug">
            </router-link>
        </ul>
    </div>
</template>

<script>
export default {
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
        works() {
            return this.$store.state.works
        }
    }
}
</script>