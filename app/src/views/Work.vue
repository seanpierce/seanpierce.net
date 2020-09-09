<template>
    <div id="work">
        <ul>
            <li v-html="formatContent('introtorhythm.com')"></li>
            <li v-html="formatContent('spoilerroom.net')"></li>
            <li v-html="formatContent('symbiotic pulse system')"></li>
            <li v-html="formatContent('Solo Work')"></li>
            <li v-html="formatContent('ASSS')"></li>
            <li v-html="formatContent('Dutch Bros')"></li>
            <li v-html="formatContent('Hot Face')"></li>
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
    }
}
</script>