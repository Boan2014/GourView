<template>
  <div class="bg">
    <div class='bottons'>
    <div>
     <apexcharts width="500" type="bar" :options="chartOptions" :series="series"></apexcharts>
    </div>

    <div class='header'>
      <img class='image' @click="Home" src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'></img>
      <input class="normal-textbox" @keyup.enter="Search" v-model="$store.state.name" style="border-radius:80px">
        
          <v-btn class='botton1' @click="Search">Search</v-btn>
          <v-btn class='botton2' @click="clear">clear</v-btn>
        <v-divider></v-divider> 
    </div>

    <wordcloud v-if="$store.state.predictLabel"
      :data="$store.state.predictLabel"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
    </wordcloud>

    <vc-donut v-if="$store.state.posPercent"
    :sections="[{value: $store.state.posPercent}, { value:$store.state.negPercent}]">　{{ message }}</vc-donut>
    

    <h5>{{ $store.state.posPercent }}</h5>
    <h5>{{ $store.state.negPercent }}</h5>


    <h5>{{ $store.state.posRev }}</h5>

    <h5>{{ $store.state.negRev }}</h5>
    
    </div>
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
    Home(){       
     this.$router.push('/')
       },     
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
      //sections: [{ value: this.$store.state.posPercent}, { value: this.$store.state.negPercent}]

    }
  },
}

</script>
<style scoped>
  .bg {
   background-color:white;
   height:100vh;
   text-align:center;
   

  }
  .buttons{
    text-align:center;
  }

  .botton1{
   width:30px;
   margin-right:16px;
   text-align:center;
    
  }
  .botton2{
   width:30px;
   margin-right:16px;
   text-align:center;
    
  }
  .header{
  display:flex;
  align-items: center;
  padding-top: 1px;
  text-align:center;

  }

  .normal-textbox {
    color:#000000;
    background-color: #f5f4f1;
    border:1px black solid;
    width:40%;
    height: 30px;
    margin-right:16px;
    text-align:center;
  }

  .image{
    width:55px;
    margin-right:8px;
    text-align:center;

  }

  
  .homepage{
    color:rgba(20, 4, 4, 0.5);
    text-align:right;
    width:98%;
  }

  </style>

