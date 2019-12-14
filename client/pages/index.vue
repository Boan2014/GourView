<template>
  <div class="search bg">

    

    <div id="background">
    <h1 class="title">{{message}}</h1>
    <h1 class="subtitle">Explor with a single glance</h1>
    </div>
<div id="button-area2">
    <input class="normal-textbox" v-model="$store.state.name">
    </div>

<div id="button-area">
    <v-btn @click="Search">Search</v-btn>
    <v-btn @click="clear">clear</v-btn>


</div>

<div v-if="ChangePage" ></div>

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

    <p class="aboutpage">
      <NuxtLink to="/about">
        About page
      </NuxtLink>
    </p>
     <p class="aboutpage">
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
      console.log('test')
      this.isSearch= true
      this.$router.push('/afterSearch')

    

      // axios.post("http://localhost:5045/api/predict", {
      //     name: this.$store.state.name
      //   }).then((response) => {this.$store.commit('setPredictLabel', response.data.result)}).catch()
      
      
      
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
  .search {
  text-align: center;
  }
  .bg {
  background-color:rgb(245, 245, 243);
  
  }
  #button-area {
    padding-top: 30px;
  }
  #button-area2 {
    padding-top: 50px;
  }
  #background {

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
  }
  .subtitle{
    font-family:'Trebuchet';
    font-size:1.5rem;
    color:rgb(243, 89, 18);
   
    
  }
  
</style>