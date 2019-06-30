<template>
  <div class="container" id="app">
    <b-input placeholder="Host Name/IP" v-model="hostname" type="text"></b-input>
    <b-button v-on:click="checkHost">Check</b-button>
    <p>Host up: {{host_up}}</p>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      hostname: "",
      host_up: false,
    }
  },
  methods: {
    update: function() {
      this.axios.get('/api/update').then((response) => {
          console.log(response.data)
      })
    },
    checkHost: function(hostname) {
      this.host_up = "Checking..."
      this.axios.get('/api/check_host', { 
          params: {
            'hostname': this.hostname
          } 
      }).then((response) => {
          this.host_up=response.data.up
      }).catch((error) => {
        this.host_up = "Failed getting status with " + error
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
