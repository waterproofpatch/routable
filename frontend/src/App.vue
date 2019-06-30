<template>
  <div class="container" id="app">
    <b-input value="8.8.8.8" placeholder="Host Name/IP" v-model="newHostname" type="text"></b-input>
    <b-button v-on:click="updateHosts">Add</b-button>

    <b-list-group> 
      <b-list-group-item v-bind:key="host.hostname" v-for="(host, i) in hosts">Host: {{host.hostname}} Up: {{host.up}} <b-button v-on:click="checkHostAtIndex(i)">Refresh</b-button></b-list-group-item>
    </b-list-group>
  <li

  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      newHostname: "",
      hosts: []
    }
  },
  methods: {
    updateHosts: function() {
      console.log('updating...')
      this.hosts.push({'hostname': this.newHostname, 'up': false})
      console.log(this.hosts)
    },
    checkHostAtIndex: function(index) {
      this.axios.get('/api/check_host_at_index', { 
          params: {
            'hostname': this.hosts[index].hostname
          } 
      }).then((response) => {
        this.hosts[index].up = response.data.up
      }).catch((error) => {
      })
    },
    checkHost: function(hostname) {
      this.axios.get('/api/check_host', { 
          params: {
            'hostname': this.hostname
          } 
      }).then((response) => {
        this.hosts[this.hostname]=response.data.up
      }).catch((error) => {
        console.log(error)
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
