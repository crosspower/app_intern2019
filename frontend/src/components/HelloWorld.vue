<template>
  <v-container height="20000px">
    <v-layout text-center wrap></v-layout>
    <v-parallax dark src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg" height="30px">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin mb-4">Summer Intern2019</h1>
        <h4 class="subheading">Crawling enormous NETWORK today!</h4>
      </v-layout>
    </v-parallax>
    <!-- <v-flex xs12>
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        ></v-img>
    </v-flex>-->
    <v-layout>
      <v-flex xs12 sm4 text-center>
        <div class="my-2">
          <input type="text" v-model="word">
          <v-btn depressed small @click="request">Normal</v-btn>
        </div>
      </v-flex>
      {{datas}}
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    message: "Hello Vue!",
    datas: null,
    word: ""
  }),
  methods: {
    request: function() {
      let data = { search_word: this.word };
      axios({
        method: "POST",
        url: "http://localhost:8000",
        data: data
      })
        .then(response => (this.datas = response))
        .catch(error => console.log(error));
    }
  }
};
</script>
