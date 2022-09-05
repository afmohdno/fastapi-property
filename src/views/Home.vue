<template>
	<ContentLayout class="flex-grow">
		<div>
			<p class="text-center">status: {{status.status}}</p>
		</div>
		<div class="mt-20 sm:mt-40 bg-gray-700 w-full xl:w-1/2 h-72 mx-auto rounded mb-4">
			<div class="flex flex-grow items-center justify-center h-full">
				<input class="px-4 py-2 w-3/4 my-auto rounded bg-slate-100" type="text" name="" v-model="query" @keyup.enter="searchQuery" placeholder="Find property">
			</div>
		</div>
		<div v-if="results">
			<!-- plural results -->
			<template v-if=" results.length > 1 ">
				<p class="mb-4">Showing {{results.length}} results</p>
			</template>
			<!-- singular result -->
			<template v-else>
				<p class="mb-4">Showing {{results.length}} result</p>
			</template>
			<template v-if="typeof results == 'object'">
				<div class="bg-gray-200 rounded p-4 mb-2" v-for="result in results" :key="result._id">
					<div>
						<router-link :to="{ name: 'property', params: { id: result._id }}">
							<h2 class="text-xl hover:underline hover:text-blue-800">{{result.TITLE}}</h2>
						</router-link>
						<span class="text-xs text-gray-700">{{result.TENURE}}</span>
					</div>
					<p class="text-sm">from RM {{result.PRICE_RM_MIN.toLocaleString()}}</p>
				</div>
			</template>
			<template v-else>
				{{results}}
			</template>
		</div>
	</ContentLayout>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import ContentLayout from '../components/ContentLayout.vue'

const status = ref({})
const query = ref("")
const results = ref(null)

onMounted(async () => {
	await axios.get("http://localhost:8000/")
	.then(response => {
		status.value = response.data
	})
	.catch(err => {
		console.log(err)
	})
})

const searchQuery = computed( async() => {
	if (query.value) {
		await axios.get(`http://localhost:8000/property/name/${query.value}`)
		.then(response => {
			results.value = response.data
			console.log(results.value)
		})
		.catch(err => {
			console.log(err)
		})
	} else {
		results.value = null
	}
})

</script>
