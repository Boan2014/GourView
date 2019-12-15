<template>
  <div class="search bg">

    <div class="background">
    <h1 class="title">{{message}}</h1>
    <h1 class="subtitle">Explor with a single glance</h1>
    </div>

    <div class="button-area2">
        <input class="normal-textbox" @keyup.enter="Search" v-model="$store.state.name" style="border-radius:80px">
    </div>

    
      <v-btn class="button1" @click="Search">Search</v-btn>
      <v-btn class="button2" @click="clear">clear</v-btn>
    

    <p class="aboutpage">
      <NuxtLink to="/about">
        About page
      </NuxtLink>
    </p>
     <p class="Githubpage">
      <NuxtLink to="/github">
        Github
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
      //this.isSearch= true
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
      //isSearch:false,

    }
  },
}
</script>

<style scoped>
  .search {
  text-align: center;
  }
  .bg {
  background-color:rgb(245, 245, 243);

  }
  .button1 {
    padding-top: 30px;
    margin-right: 15px;
    
   
  }
  .button2 {
    padding-top: 30px;
    margin-right: 15px;
    
   
  }

  .button-area2 {
    padding-top: 10px;
    margin-bottom: 7px;
    
  }
  .background {

    background-image:url("~@/static/BK_04.jpg");
    background-size:100%;
    height: 25rem;
    padding-top: 130px;
    text-align:center;

      }

  .normal-textbox {
    color:#000000;
    background-color: rgb(245, 245, 243);
    border:1px rgb(201, 67, 4) solid;
    width:500px;
    height: 50px;
  }
  .title{
    color:rgb(243, 89, 18);
    font-size: 5rem !important;
  }
  .aboutpage{
    background-color:rgba(34, 33, 33, 0.5);
    text-align:right;
    margin-top: 30px;
  }
  .Githubpage{
    background-color:rgba(34, 33, 33, 0.5);
    text-align:right;
    margin-bottom: 0px;
  }
  .subtitle{
    font-family:'Trebuchet';
    font-size:1.5rem;
    color:rgb(243, 89, 18);


  }

</style>