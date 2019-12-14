<template>
  <div class="search bg">
    
    <div id="button-area3">
      <h3 class="title">{{message}}</h3>
    </div>

    <div id="button-area2">
        <input class="normal-textbox" @keyup.enter="Search" v-model="$store.state.name" style="border-radius:80px">
    </div>

    <div id="button-area">
      <v-btn @click="Search">Search</v-btn>
      <v-btn @click="clear">clear</v-btn>
    </div>


  <img v-if="loadig" src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'></img>
  <div v-if="loadig">Searching・・・・</div>

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
      console.log('test')
      this.loading= true
      this.$router.push('/afterSearch')
      axios.post("http://localhost:5045/api/predict", {
          name: this.$store.state.name
        }).then((response) => {this.$store.commit('setPredictLabel', response.data.result),this.loading = false})
    },
    
  },
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      message:"GOURVIEW",
      isSearch:false,
      ChangePage:false,
      loading: false,
    }
  },
}
</script>

<style scoped>
  .search {
  text-align: center;
  }
  .bg {
  background-image:url("~@/static/BK_01.jpg");
  background-size: cover;
  }
  #button-area {
    padding-top: 30px;
  }
  #button-area2 {
    padding-top: 50px;
  }
  #button-area3 {
    padding-top: 200px;
    color:rgb(11, 12, 11);
      }
  
  .normal-textbox {
    color:#000000;
    background-color: #f5f4f1;
    border:1px black solid;
    width:600px;
    height: 50px;
  }
  .title{
    background-color:burlywood;
    color:black;
    font-size: 4rem;
    line-height: 5rem;
    
  }

  
  .aboutpage{
    background-color:rgba(34, 33, 33, 0.5);
    text-align:right;
    text-decoration: none !important;
  }
  
</style>