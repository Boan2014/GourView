<template>
  <div class="bg">
    <div class='header'>
      <img class='image' src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'></img>
      <input class="normal-textbox" v-model="$store.state.name">
        <div class='botton'>
          <v-btn @click="Search">Search</v-btn>
          <v-btn  @click="clear">clear</v-btn>
        </div>
    </div>

    <wordcloud v-if="$store.state.predictLabel"
      :data="$store.state.predictLabel"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
    </wordcloud>

    <p class="homepage">
      <NuxtLink to="/">←Home</NuxtLink>
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
      // console.log('test')
      // this.isSearch= true
      // this.$router.push('/afterSearch')
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
      message:"GOURVIEW",
      isSearch:false,
      ChangePage:false,
      dummy:[{"name":"おいしい","value":3}]

    }
  },
}

</script>
<style scoped>
  .bg {
   background-color:lightcyan;
   height:100vh;

  }

  .botton{
   width:15rem;
   margin-right:8px;
    
  }

  .header{
  display:flex;
  align-items: center;
  padding-top: 1px;

  }

  .normal-textbox {
    color:#000000;
    background-color: #f5f4f1;
    border:1px black solid;
    width:200px;
    height: 30px;
    margin-right:16px;
  }

  .image{
    width:100px;
    margin-right:8px;
    

  }

  
  .homepage{
    color:rgba(20, 4, 4, 0.5);
    text-align:right;
    width:98%;
  }

  </style>

