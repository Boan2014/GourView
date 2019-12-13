<template>
  <div class="search">

    
   <v-btn  @click="Move">retty</v-btn>
    <v-btn  @click="Search">hh</v-btn>
    <v-btn @click="clear">clear</v-btn>
     <nuxt-link to="/about" > About</nuxt-link>
    <v-text-field id="textbox" v-model="$store.state.name"></v-text-field>
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
  },
  methods:{
    Search: function(){
      textbox.moveTo(200, 100);
      textbox.focus();
    },
    Move: function(){
    location.href = 'https://retty.me/theme/101041400/';

}    

  }
}
</script>

<style scoped>
  .search {
  text-align: center;
  }

  .textbox{
  padding-top: 500px;

 ;


}
</style>