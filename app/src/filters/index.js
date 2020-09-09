import Vue from 'vue'

// wraps specified letters in a spac with a class 
// that changes the font family of the character
Vue.filter('formatFont', value => {
    const letters = ['s', 'p']
    let text = strip(value)
    let stringArray = text.split('')
    stringArray.forEach((character, index) => {
        if (letters.indexOf(character.toLowerCase()) > -1)
            stringArray[index] = `<span class="yolda">${character}</span>`
    });
    return stringArray.join('')
})

let strip = (html) => {
    var doc = new DOMParser().parseFromString(html, 'text/html');
    return doc.body.textContent || '';
}