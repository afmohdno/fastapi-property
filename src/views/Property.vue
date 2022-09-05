<template>
	<ContentLayout>
		<div class="bg-gray-200 p-4 text-gray-800 rounded">
			<h2 class="text-2xl">{{ property.TITLE }}</h2>
			<span>{{ property.TENURE }}</span>
			<div class="mt-4">
				<p>Type: {{ property.PROPERTY_TYPE }}</p>
				<p class="text-slate-500">{{ props.id }}</p>
			</div>
		</div>
	</ContentLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ContentLayout from '../components/ContentLayout.vue'

const property = ref({})
const props = defineProps(['id'])
console.log(property.value.length)

onMounted( async() => {
	await axios.get(`http://localhost:8000/property/${props.id}`)
	.then(response => {
		property.value = response.data
		console.log("data retrieved")
	})
	.catch(err => {
		console.log(err)
	})
})
</script>

<style lang="css" scoped>
</style>