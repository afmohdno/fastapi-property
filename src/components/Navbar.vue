<template>
	<nav class="bg-stone-600">
		<div class="container flex items-center justify-between py-4 px-3 mx-auto text-slate-300 font-bold">
			<div>
				<router-link :to="{ name: 'home'}" class="hover:text-slate-100 px-3 py-2">Property</router-link>
			</div>
			<div>
				<a class="hover:text-slate-100" href="">Login</a>
			</div>
		</div>
	</nav>
</template>

<script setup>
</script>

<style lang="css" scoped>
</style>