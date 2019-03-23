<template>
	<div id="app">
		<navbar/>
		<b-container fluid>
			<b-row>
				<b-col>
					<router-view/>
				</b-col>
			</b-row>
		</b-container>
	</div>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
	name: "App",
	components: {
		Navbar
	}
};
</script>

<style>
#app {
	font-family: "Avenir", Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}
</style>
