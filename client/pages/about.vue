<template>
 <div class="bg">
    <p >
    <NLink to="/">
      Home page
    </NLink>
    </p>
   <h1 class="title">{{message}}</h1>

   <p class="introduce"> 
     aa 
     </br> 
     bb 
     </p>
   
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