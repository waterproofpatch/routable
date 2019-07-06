<template>
  <div class="container" id="app">
    <b-input-group prepend="Username" class="mt-3">
      <b-form-input placeholder="Host Name/IP" v-model="newHostname"></b-form-input>
      <b-input-group-append>
        <b-button variant="outline-success" v-on:click="updateHosts">Add</b-button>
      </b-input-group-append>
    </b-input-group>

    <b-list-group> 
      <b-list-group-item v-bind:key="host.hostname" v-for="(host, i) in hosts">
        Host: {{host.hostname}} Up: {{host.up}} 
        <b-button v-on:click="checkHostAtIndex(i)">
          Refresh
        </b-button>
        <b-button v-on:click="hosts.splice(i, 1)">
          Remove
        </b-button>
      </b-list-group-item>
    </b-list-group>
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
      this.hosts.push({'hostname': this.newHostname, 'up': false})
      this.checkHostAtIndex(this.hosts.length - 1)
    },
    checkHostAtIndex: function(index) {
      this.hosts[index].up = 'Checking...'
      this.axios.get('/api/check_host', { 
        params: {
          'hostname': this.hosts[index].hostname
        } 
      }).then((response) => {
        this.hosts[index].up = response.data.up
      }).catch((error) => {
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
