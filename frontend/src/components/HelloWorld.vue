<template>
  <v-container class="pa-0" align-center fluid>
    <!-- <v-layout text-center wrap></v-layout> -->
    <v-parallax dark height="300" src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin mb-10 mt-10">Summer Intern2019</h1>
        <v-flex>
          <v-text-field label="Here comes a word" color="white" outlined v-model="word"></v-text-field>
          <v-btn
            large
            depressed
            small
            @click="request"
            :loading="loading"
            :disabled="loading"
            color="primary"
          >search</v-btn>
        </v-flex>
      </v-layout>
    </v-parallax>
    <v-layout class="pa-5 d-block">
      <v-flex class="pl-5" v-if="product_infos">{{search_word}}の検索結果</v-flex>
      <v-flex class="pl-5" v-if="product_infos">{{product_infos.length}}件表示</v-flex>
      <v-flex md12 text-center v-if="product_infos">
        <v-row>
          <v-col cols="12">
            <v-row justify="center">
              <item-box
                v-for="(item,index) in product_infos"
                :key="index"
                class="mr-10 mb-10"
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
    word: "",
    display_word: "",
    loading: false
  }),
  components: {
    "item-box": ItemBox
  },
  methods: {
    request: function() {
      this.loading = true;
      this.search_word = this.word;
      let data = { search_word: this.word };
      axios({
        method: "POST",
        url: "http://localhost:8000",
        data: data
      })
        .then(response => (this.product_infos = response.data))
        .catch(error => console.log(error))
        .finally(() => (this.loading = false));
    }
  }
};
</script>