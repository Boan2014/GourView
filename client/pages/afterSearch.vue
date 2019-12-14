<template>
<div class="bg">
<div class='header'>


<img  class='image' @click="Home"  src='@/assets\img\{684FC80B-7F42-48CE-8416-F7FB9B6F8248}.png.jpg'></img>
<input class="normal-textbox" v-model="$store.state.name" style="border-radius:80px">

<div class='botton'>
<v-btn @click="Search">Search</v-btn>
<v-btn   @click="clear">clear</v-btn>
</div>

</div>
<p v-divider></p>
 <p class="homepage">
   <NuxtLink to="/">
  ←Home
   </NuxtLink>
   </p>


</div>

</template>

<script>
export default {
methods: {
    Home(){       
     this.$router.push('/')
       },     
    },
}

 </script>

<style scoped>
  .bg {
   background-color:lightcyan;
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

  
  .homepage{
    color:rgba(20, 4, 4, 0.5);
    text-align:right;
    width:98%;
  }

  </style>

