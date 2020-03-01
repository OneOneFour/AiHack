<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <l-map :centre="[-55,0]" :zoom="4">
            <l-choropleth-layer :data=""
        </l-map>

    </div>
</template>

<script>
    import {LMap} from "vue2-leaflet";
    import {InfoControl, ReferenceChart, ChoroplethLayer} from 'vue-choropleth';

    export default {
        name: 'App',
        components: {
            LMap, 'l-info-control': InfoControl,
            'l-reference-chart': ReferenceChart,
            'l-choropleth-layer': ChoroplethLayer

        },
        data() {
            return {
                geoJson: "https://opendata.arcgis.com/datasets/5252644ec26e4bffadf9d3661eef4826_4.geojson"
                value: {
                    key: "sum_drugs_5_years"
                }
            }
        },
        methods: {
            fetch_ccg_data() {
                const url = "http://aihack2020.appspot.com/api/ccg";
                fetch(url)
                    .then(response => {
                        return response.json()
                    })
                    .then(data => {
                        this.ccg_data = data
                    })
            }
        },
        mounted() {
            this.fetch_ccg_data();
        }
    }
</script>

<style lang="scss">
    @import "~leaflet/dist/leaflet.css";

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
