<template>
  <div class="h-screen flex flex-col">
		<Navbar/>
	  <slot/>
  	<Footer/>
  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
</style>
