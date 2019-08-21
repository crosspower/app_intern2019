<template>
  <v-container class="pa-0 ma-0 item-box">
    <v-layout class="d-block">
      <v-flex pa-0>
        <v-img
          :src="product_info['image']"
          aspect-ratio="1"
          class="grey lighten-2"
          max-height="160"
          max-width="160"
          position="top"
        ></v-img>
      </v-flex>
      <v-flex pa-2 class="product-detail">
          <h5 class="product-title">{{product_info['title']}}</h5>
          <div class="mt-1" >¥{{product_info['price']}}</div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  props: ["product_info"],
  data: () => ({
    message: "herehere"
  })
};
</script>
<style>
.item-box{
    width:160px !important;
    height:300px !important;
}
.product-detail{
    background-color:white;
}
.product-title{
    height:65px;
    overflow:hidden;
}
</style>