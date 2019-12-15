<template>
  <div class="search bg">
    

    <div id="background">
    <h1 class="title">{{message}}</h1>
    <h1 class="subtitle">Explor with a single glance</h1>
    </div>

    <div id="button-area2">
        <input class="normal-textbox" @keyup.enter="Search" v-model="$store.state.name" style="border-radius:80px">
    </div>

    <div id="button-area">
      <v-btn @click="Search">Search</v-btn>
      <v-btn @click="clear">clear</v-btn>
    </div>

  <div v-if="ChangePage" ></div>

    <p class="aboutpage">
      <NuxtLink id="github" to="/github">
        Github
      </NuxtLink>
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
      this.isSearch= true
      this.$router.push('/afterSearch')
      axios.post("http://localhost:5045/api/predict", {
          name: this.$store.state.name
        }).then((response) => {this.$store.commit('setPredictLabel', response.data.result)})
    }
  },
  data() {
    return {
      myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
      message:"GOURVIEW",
      isSearch:false,
      ChangePage:false,
    }
  },
}
</script>

<style scoped>
  .search {
  text-align: center;
  }
  .bg {
  background-color:white;
  
  }
  #button-area {
    padding-top: 30px;
    padding-bottom:20rem
  }
  #button-area2 {
    padding-top: 50px;
  }
  #background {

    background-image:url("~@/static/BK_04.jpg");
    background-size:100%;
    height: 20rem;
    padding-top: 130px;
    text-align:center;
    
      }
  
  .normal-textbox {
    color:#000000;
    background-color: white;
    border:1px rgb(201, 67, 4) solid;
    width:500px;
    height: 50px;
  }
  .title{
    color:rgb(243, 89, 18);
    font-size: 5rem !important;
    text-shadow:3px 3px 2px #181004
  }
  .aboutpage{
    background-color:rgba(108, 153, 143, 0.4);
    text-align:center;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight:400;
    padding-bottom: 0px;
    height:2rem;
    padding-top:6px;
  }
  .aboutpage a {
    text-decoration: none;
  }
  #github{
    padding-right:5%
  }
  .subtitle{
    font-family:'Trebuchet';
    font-size:1.5rem;
    color:rgb(196, 84, 40);
    text-shadow:1px 1px 1px #2c1c04
   
    
  }
  
</style>