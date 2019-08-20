<template>
  <v-container class="pa-0" align-center>
    <!-- <v-layout text-center wrap></v-layout> -->
    <v-parallax dark height="300" src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin mb-10 mt-10">Summer Intern2019</h1>
        <v-flex>
          <v-text-field label="Here comes a word" outlined v-model="word"></v-text-field>
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
    <v-layout>
      <v-flex md12 text-center v-if="datas">
            <item-box :product_info="item" v-for="(item,index) in datas[1]['item']" :key="index"></item-box>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ItemBox from "./ItemBox.vue";
import axios from "axios";
export default {
  data: () => ({
    datas: null,
    word: "",
    loading: false
  }),
  components: {
    "item-box": ItemBox
  },
  methods: {
    request: function() {
      this.loading = true;
      let data = { search_word: this.word };
      axios({
        method: "POST",
        url: "http://localhost:8000",
        data: data
      })
        .then(response => (this.datas = response.data))
        .catch(error => console.log(error))
        .finally(() => (this.loading = false));
    }
  }
};
</script>
