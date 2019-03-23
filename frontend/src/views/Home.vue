<template>
	<div class="home">
		<b-container fluid>
			<b-row style="background-color:#e0e0e0">
				<b-col>
					<h1>I made this Vue App</h1>
					<ul id="example-1">
						<li v-for="item in items" :key="item.id">{{ item.message }}</li>
					</ul>
				</b-col>
			</b-row>
		</b-container>
	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
	name: "home",
	components: {
		HelloWorld
	},
	data() {
		return {
			parentMsg: "Hello",
			items: [{ id: 0, message: "Foo" }, { id: 1, message: "Bar" }]
		};
	}
};
</script>
