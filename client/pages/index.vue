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
  background-image:url("http://img1.juimg.com/180104/355840-1P10404223646.jpg");
  width:200vh !important;
  
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
    width:500px;
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
  }
  
</style>