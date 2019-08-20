<template>
  <v-container height="20000px">
    <!-- <v-layout text-center wrap></v-layout> -->
    <v-parallax dark height="300" src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
      <v-layout align-center column justify-center>
        <h1 class="display-2 font-weight-thin mb-10 mt-10">Summer Intern2019</h1>
        <div class="mb-4">
          <input type="text" v-model="word" placeholder="Here comes a word"/>
          <v-btn depressed small @click="request" :loading="loading" color="primary">search</v-btn>
        </div>
      </v-layout>
    </v-parallax>
    <v-layout>
      <v-flex md12 text-center>
        <div class="my-2">{{datas}}</div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    message: "Hello Vue!",
    datas: null,
    word: "",
    loading: false
  }),
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
