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
      <toggle-p>Toggle Switch</toggle-p>
        <div class="toggle-switch">
          <toggle-input id="toggle" class="toggle-input" type='checkbox' />
          <label for="toggle" class="toggle-label"/>
        <span></span>
        </div>
        
    </div>
    <br>
    <v-divider></v-divider> 
    
    <h1>{{ $store.state.shopName }}</h1>

    <wordcloud v-if="$store.state.predictLabel"
      :data="defaultWords"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
    </wordcloud>

    <br>
    <v-divider></v-divider> 
    <img v-if="$store.state.predictLabel===0"  src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'/>

    <div>

      <img class='emoji' v-if="$store.state.posPercent || $store.state.negPercent" src="https://raw.githubusercontent.com/Boan2014/Warehouse/master/Other/good.gif">{{ $store.state.posPercent }}</img>

      <vc-donut :size=200 thickness=40 v-if="$store.state.posPercent || $store.state.negPercent"
      :sections="[{value: $store.state.posPercent}, { value:$store.state.negPercent}]">　<img class='image' @click="Home" src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'/></vc-donut>
      
      <img class='emoji' v-if="$store.state.posPercent || $store.state.negPercent" src="https://raw.githubusercontent.com/Boan2014/Warehouse/master/Other/hate.gif">{{ $store.state.negPercent }}</img>

    <div class="graph">
     <button class="btn-blue">
      <img class='emoji1' v-if="true" src="https://raw.githubusercontent.com/Boan2014/Warehouse/master/Other/hate.gif">80%</img>
     </button>
      <vc-donut :size=250 thickness=40 v-if="true"
      :sections="[{value: 20}, { value:80}]">　<img class='image' @click="Home" src='https://4.bp.blogspot.com/-aJjlevJyK9U/XGjx40QThrI/AAAAAAABRco/j9aRPnYHpX4PU6RZjhTWRh6_8xnPfbNEQCLcBGAs/s800/animal_chara_computer_azarashi.png'/></vc-donut>
     <button class="btn-red">
      <img class='emoji2' v-if="true" src="https://raw.githubusercontent.com/Boan2014/Warehouse/master/Other/good.gif">20%</img>
     </button>
    </div>

    <h5>{{ $store.state.posPercent }}</h5>
    <h5>{{ $store.state.negPercent }}</h5>
    
    </div>
    <p class="homepage">
      <NuxtLink to="/">←Home</NuxtLink>
   </p>
  </div>
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
      defaultWords: [{
          "name": "Cat",
          "value": 26
        },
        {
          "name": "fish",
          "value": 19
        },
        {
          "name": "things",
          "value": 18
        },
        {
          "name": "look",
          "value": 16
        },
        {
          "name": "two",
          "value": 15
        },
        {
          "name": "fun",
          "value": 9
        },
        {
          "name": "know",
          "value": 9
        },
        {
          "name": "good",
          "value": 9
        },
        {
          "name": "play",
          "value": 6
        }
      ],
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
  justify-content:center;

  }

  .normal-textbox {
    color:#000000;
    background-color: #f5f4f1;
    border:1px black solid;
    width:40%;
    height: 30px;
    margin-right:16px;
    padding-left: 8px;
    outline:none;
  }

  .image{
    width:55px;
    margin-right:8px;
  }
  .toggle-input {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  z-index: 5;
  opacity: 0;
  cursor: pointer;
}

label {
  width: 75px;
  height: 42px;
  background: #ccc;
  position: relative;
  display: inline-block;
  border-radius: 46px;
  transition: 0.4s;
  box-sizing: border-box;
}
label:after {
  content: '';
  position: absolute;
  width: 42px;
  height: 42px;
  border-radius: 100%;
  left: 0;
  top: 0;
  z-index: 2;
  background: #fff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  transition: 0.4s;
}

input:checked + label {
  background-color: #4BD865;
}
input:checked + label:after {
  left: 40px;
}

toggle-p {
  margin-top: 50px;
  text-align: center;
  font-weight: bold;
}

.toggle-switch {
  position: relative;
  width: 75px;
  height: 42px;
  margin: auto;
}


  .btn-blue{
    padding: 0.25em 0.75em;
    margin: 2em 0;
    color: #FFF;
    background: #36A2EB;
    border-bottom: solid 6px #1F77B4;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25);
    border-radius: 9px;
    margin-right: 16px;
    outline:none;

  }
  .btn-blue:active {
  /*ボタンを押したとき*/
  -webkit-transform: translateY(4px);
  transform: translateY(4px);/*下に動く*/
  border-bottom: none;/*線を消す*/
}
  .btn-red{
    padding: 0.25em 0.75em;
    margin: 2em 0;
    color: #FFF;
    background: #FF6384;
    border-bottom: solid 6px #CF486A;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25);
    border-radius: 9px;
    margin-left: 16px;
    outline:none;
    
  }
   .btn-red:active {
  /*ボタンを押したとき*/
  -webkit-transform: translateY(4px);
  transform: translateY(4px);/*下に動く*/
  border-bottom: none;/*線を消す*/
  }


  .graph{
    display:flex;
    align-items: center;
    justify-content:center;
    padding-top: 5px;

  }

  .emoji1{
    width:50px;
    margin-bottom: 0px;
    

  }
  .emoji2{
    width:50px;
     

  }
  
  .homepage{
    color:rgba(20, 4, 4, 0.5);
    text-align:right;
    width:98%;
  }

  </style>

