<template>
  <div class="search">

    <v-text-field v-model="$store.state.name"></v-text-field>

    <v-btn @click="Search">Search</v-btn>
    <v-btn @click="clear">clear</v-btn>

    <wordcloud v-if="$store.state.predictLabel"
      :data="$store.state.predictLabel"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
    </wordcloud>

  </div>

</template>

<script>
import axios from "axios";
import wordcloud from 'vue-wordcloud';
export default {
  head: {
    title: 'Home page'
  },
  components: {
    wordcloud
  },
  methods :{
    // 入力値を初期値に戻すメソッド
    clear (){
      this.$store.commit('clear')
    },
    // APIを叩くメソッド
    Search() {
      axios.post("http://localhost:5045/api/predict", {
          name: this.$store.state.name
        }).then((response) => {this.$store.commit('setPredictLabel', response.data.result)})
      },
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    }
  },
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    }
  }
}
</script>

<style scoped>
  .search {
  text-align: center;
}
</style>