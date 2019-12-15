<template>
  <div class="bg">

    <div>
     <apexcharts width="500" type="bar" :options="chartOptions" :series="series"></apexcharts>
    </div>
    
    <div class='header'>
      <img class='image' @click="Home" src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'/>
      <input class="normal-textbox" v-model="$store.state.name" style="border-radius:80px">
        <div class='botton'>
          <v-btn @click="Search">Search</v-btn>
          <v-btn  @click="clear">clear</v-btn>
        </div>
    </div>
    
    <h1>{{ $store.state.shopName }}</h1>

    <wordcloud v-if="$store.state.predictLabel"
      :data="$store.state.predictLabel"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
    </wordcloud>

    <img v-if="$store.state.predictLabel===0"  src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'/>

    <div>

      <img class='emoji' v-if="$store.state.posPercent || $store.state.negPercent" src="https://raw.githubusercontent.com/Boan2014/Warehouse/master/Other/good.gif">{{ $store.state.posPercent }}</img>

      <vc-donut :size=200 thickness=40 v-if="$store.state.posPercent || $store.state.negPercent"
      :sections="[{value: $store.state.posPercent}, { value:$store.state.negPercent}]">　<img class='image' @click="Home" src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'/></vc-donut>
      
      <img class='emoji' v-if="$store.state.posPercent || $store.state.negPercent" src="https://raw.githubusercontent.com/Boan2014/Warehouse/master/Other/hate.gif">{{ $store.state.negPercent }}</img>

    </div>
    <h5>{{ $store.state.posPercent }}</h5>
    <h5>{{ $store.state.negPercent }}</h5>
    
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
      
      this.$store.commit('clear')

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

  }

  .botton{
   width:15%;
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
    width:60%;
    margin-right:16px;
  }

  .image{
    width:20%;
    margin-right:8px;
  }

  .emoji{
    width:5%;
    margin-left:100px;
    

  }

  
  .homepage{
    color:rgba(20, 4, 4, 0.5);
    text-align:right;
    width:98%;
  }

  </style>

