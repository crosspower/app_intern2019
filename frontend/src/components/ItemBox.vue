<template>
  <v-container class="pa-0 ma-0 item-box">
    <v-layout class="d-block" @click="open_link">
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
        <div class="mt-1">
          <v-row class="mx-2">
            ￥{{`${(product_info['price']||'-').toLocaleString('ja-JP')}`}}
            <v-spacer></v-spacer>
            <v-img :src="product_info['icon']" max-height="30" max-width="30"></v-img>
          </v-row>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  props: ["product_info"],
  methods: {
    open_link() {
      window.open(this.product_info["link"], "_blank");
    }
  }
};
</script>
<style>
.item-box {
  width: 160px !important;
  height: 300px !important;
}
.product-detail {
  background-color: white;
}
.product-title {
  height: 4.3em;
  overflow: hidden;
  position: relative;
}
.product-title::after {
  display: block;
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50%;
  height: 1.5em;
  background: -webkit-gradient(
    linear,
    left top,
    right top,
    from(rgba(255, 255, 255, 0)),
    color-stop(72%, #fff)
  );
  background: linear-gradient(to right, rgba(255, 255, 255, 0), #fff 72%);
}
</style>