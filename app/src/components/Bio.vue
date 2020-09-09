<template>
    <div id="bio" class="hel-out" v-html="formatBio"></div>
</template>

<script>
export default {
    data() {
        return {
            bio: 'Sean Pierce is an artist and musician working in Portland, OR. Pierce has released music on labels based in London, Berlin, Glasgow, Chicago, Los Angeles, and Seattle, and he has performed in many cities across North America and Europe.'
        }
    },
    computed: {
        formatBio() {
            let stringArray = this.bio.split('')
            stringArray.forEach((character, index) => {
                if (character.toLowerCase() === 's' || character.toLowerCase() === 'p')
                    stringArray[index] = `<span class="yolda">${character}</span>`
            });
            return stringArray.join('')
        }
    },
}
</script>