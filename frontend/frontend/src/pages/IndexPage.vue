<template>
  <q-page-container>
    <q-layout view="hHh lpR fFf">
      <div class="q-pa-md">
        <div class="row" v-for="question in questions" v-bind:key="question.id">
          <div class="col">
            <q-input outlined v-model="question.response" :label="question.question" /><br>
          </div>
        </div>
        <div class="row">
          <q-btn color="primary" label="Valider" @click="submitForm" />
        </div><br><br>
        <div class="row">
          <iframe id="inlineFrameExample"
            title="Inline Frame Example"
            width="100%"
            height="750px"
            src="http://localhost:8000/files/template.html">
          </iframe>
        </div>
      </div>
    </q-layout>
  </q-page-container>
</template>

<script>
import { defineComponent } from 'vue'
import { Geolocation } from '@capacitor/geolocation'

export default defineComponent({
  name: 'IndexPage',
  data () {
    return {
      questions: null
    }
  },
  methods: {
    async getQuestions () {
      const url = 'http://127.0.0.1:8000/questions'
      this.$axios.get(url)
        .then((response) => {
          this.questions = response.data.data
        })
    },
    submitForm () {
      const url = 'http://127.0.0.1:8000/questions/1'
      this.$axios.post(url, { data: this.questions })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getCurrentPosition () {
      Geolocation.getCurrentPosition().then(newPosition => {
        console.log('Current', newPosition)
      })
    }
  },
  created () {
    this.getQuestions()
    this.getCurrentPosition()
  }
})
</script>
