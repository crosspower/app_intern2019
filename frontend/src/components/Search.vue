<template>
  <v-container class="pa-0" align-center fluid>
    <v-parallax dark height="300" src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin my-10">App Intern2019</h1>
        <v-flex>
          <v-text-field
            label="Here comes a word"
            color="white"
            outlined
            v-model="search_word"
            :loading="loading"
            :disabled="loading"
            :append-icon="'mdi-magnify'"
            @keyup.enter="request"
            @click:append="request"
            class='my-text-style'
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-parallax>
    <!-- 商品情報の表示 -->
    <v-layout class="pa-5 d-block" v-if="product_infos">
      <v-flex class="pl-5">{{display_word}}の検索結果</v-flex>
      <v-flex class="pl-5">{{product_infos.length}}件表示</v-flex>
      <v-flex md12 text-center>
        <v-row>
          <v-col cols="12">
            <v-row justify="center">
              <item-box
                v-for="(item,index) in product_infos"
                :key="index"
                class="mr-10 mb-10 css-fade"
                :product_info="item"
              ></item-box>
            </v-row>
          </v-col>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ItemBox from "./ItemBox.vue";
import axios from "axios";
export default {
  data: () => ({
    product_infos: null,
    search_word: "",
    display_word: "",
    loading: false
  }),
  components: {
    "item-box": ItemBox
  },
  methods: {
    async request(){
      if (!this.search_word){
        return 
      }
      
      this.loading = true;
      this.product_infos = null;
      this.display_word = this.search_word;
      let data = { search_word: this.search_word };

      try{
        const response = await axios({
          method: "POST",
          url: "http://localhost:8000",
          data: data
        })
        this.product_infos = response.data
      } catch {
        this.product_infos = []
      }
      this.loading = false
    }
  }
};
</script>
<style scoped>
.my-text-style >>> .v-text-field__slot input {
    color: white !important;
  }
.css-fade{
  animation-name:fade-in1;
  animation-duration:2s;
  animation-timing-function: ease-out;
  animation-delay:0s; 
  animation-iteration-count:1; 
  animation-direction:normal; 
  animation-fill-mode: forwards; 
}
@keyframes fade-in1 {
  0% {
    opacity: 0;
    transform: translateY(-50px);
    -webkit-filter: blur(15px);
    -moz-filter: blur(15px);
    -ms-filter: blur(15px);
    -o-filter: blur(15px);
    filter: blur(15px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
    -webkit-filter: blur(0px);
    -moz-filter: blur(0px);
    -ms-filter: blur(0px);
    -o-filter: blur(0px);
    filter: blur(0px);
    }
}
</style>