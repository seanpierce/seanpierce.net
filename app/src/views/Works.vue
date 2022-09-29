<template>
    <div id="works">
        <!-- <ul>
            <li v-for="work in works" 
                :key="work.id">
                <router-link
                    v-html="formatContent(work.title)"
                    :to="'/works/' + work.slug">
                </router-link>
            </li>
        </ul> -->
        <div v-for="work in works" :key="work.id">
            <Work :work="work"/>
        </div>
    </div>
</template>

<script>
import Work from '@/components/Work';

export default {
    components: {
        Work
    },
    computed: {
        works() {
            return this.$store.state.works.works
        }
    }
}
</script>