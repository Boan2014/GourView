<template>
 <div class="bg">
    <p >
    <NLink to="/">
      Home page
    </NLink>
    </p>
   <h1 class="title">{{message}}</h1>

   <h1 class="introduce">日本語</h1>
   <h1 class="introduce">私たちは</h1>
    <h1 class="introduce">私たちは</h1>
     <h1 class="introduce">私たちは</h1>
      <h1 class="introduce">私たちは</h1>
   <h1 class="introduce">ENGLISH</h1>
   <h1 class="introduce">A</h1>
   <h1 class="introduce">B</h1>
   <h1 class="introduce">C</h1>
   <h1 class="introduce">D</h1>
  
   
    <div class="bg"></div>
  </div>
  
</template>

<script>
export default {
   asyncData () {
    return {
        message:"About us",
    }
  },
  head: {
    title: 'About page'
  }
}
</script>

<style scoped>
.title{
    background-color:rgba(12, 12, 12, 0.932);
    color:rgb(243, 89, 18);
    font-size: 3rem !important;
    line-height: 4rem;
}
.introduce{
  color:rgb(14, 13, 13);
  font-size: 1.5rem !important;
  
}
.bg{
  background-image:url("~@/static/BK_01.jpg");
}

</style>