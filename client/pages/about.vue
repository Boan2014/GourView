<template>
 <div class="bg">
    

 <h1 class="title">{{message}}</h1>


<h1 class="about">About</h1>

<p class="image">
<img width="85%" src="~@/static/BK_01.png">
</p>

<div id=“message”>
   <p class="introduce"> 
     Hi there! Welcome to gourview, a website specilizing in visualized restaurant reviews. Explor and find out more about your favorite restaurant.
     </p>

     <p id="homepage">
    <NLink to="/">
     | Home page |
         </NLink>
    </p>
</div>
     
   
    
  </div>
  
</template>

<script>
export default {
   asyncData () {
    return {
        message:"GOURVIEW",
    }
  },
  head: {
    title: 'About page'
  }
}
</script>

<style scoped>
.title{
    color:rgb(243, 89, 18);
    font-size: 1.7rem !important;
    line-height: 4rem;
    text-align:left;
     border-bottom: 1px solid rgb(182, 63, 8);
   margin:0% 10%;
   padding-top:1rem;

   
}
.introduce{
  color:rgb(14, 13, 13);
  font-size: 20px!important;
  text-indent: 50px;
  padding-top:5%;
  font-family:'Athelas';
   margin:10% 23%;
   font-weight: 
   
}
#message{
  padding-top:5%;
}
.bg{
  background-color:white;
}
#background{
  background-color:white;
}
#homepage{
  text-align:center;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-weight:400;
  font-size: 110%;
  color:white;
  background-color:rgba(108, 153, 143, 0.4);
  height: 3rem;
  padding-top:15px;
  
}
#homepage a {
  text-decoration: none;
}
.about{
  text-align: center;
  padding-top:50px;
  font-family:'Hiragino Maru Gothic Pro';
  font-size: 23px;
  font-weight:130;
  letter-spacing:2px;
  animation-duration: 1s;
  animation-name: slidein;
}

@keyframes slidein {
  from {
    margin-left: 100%;
    width: 300%; 
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}
.image{
  padding-top:40px;
  text-align: center;
  }
  
</style>