<template>
<div class="bg">
<div class='header'>


<input class="normal-textbox" v-model="$store.state.name">

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

