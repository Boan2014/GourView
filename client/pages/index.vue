<template>
  <div class="search">
    
    <h1 class="title">グルビュー</h1>


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

    <h1>{{ $store.state.posScore }}</h1>
    <h3>{{ $store.state.posRev }}</h3>

    <h1>{{ $store.state.negScore }}</h1>
    <h3>{{ $store.state.negRev }}</h3>

    <p>
      <NuxtLink to="/about">
        About page
      </NuxtLink>
    </p>

  </div>

</template>

<script>
import axios from "axios";
import wordcloud from 'vue-wordcloud';

export default {
  name: 'demo',
  head: {
    title: 'Home page'
  },
  components: {
    wordcloud,
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