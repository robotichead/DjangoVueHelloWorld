<template>
    <div>
        <h1>Hello World from Vue JS</h1>
        <p>Luke says HI</p>

        <!-- A SIMPLE LOOP FOR PLACES -->
        <ul>
            <li v-for="place in placesResults">
                {{place['fields']['PlaceName']}}
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "HelloWorld",
        props: [
            'placesResults',
        ],
    }
</script>

<style scoped>

</style>