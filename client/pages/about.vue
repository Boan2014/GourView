<template>
 <div class="bg">
    <p >
    <NLink to="/">
      Home page
    </NLink>
    </p>
   <h1 class="title">{{message}}</h1>
<div id=message>
   <p class="introduce"> 
     Hi there! Welcome to gourview, a website specilizing in visualized restaurant reviews. Explor and find out more about your favorite restaurant.
     </br> 
     </p>
</div>



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
    color:rgb(15, 15, 15);
    font-size: 3rem !important;
    line-height: 4rem;
    text-align:center;
}
.introduce{
  color:rgb(14, 13, 13);
  font-size: 1.5rem !important;
  text-indent: 50px;
  font-family: fantasy
}
#message{
  padding-top:5%;
}
.bg{
  background-image: linear-gradient( rgb(240, 243, 235) , rgb(153, 187, 192), rgb(97, 138, 145),rgb(62, 113, 121),rgb(44, 75, 80));
}

</style>