<template>
	<div id="app">
		<navbar/>
		<router-view/>
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
	background-color: #FFFFFF;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}

#app .container-fluid {
	/* padding-left: 0;
	padding-right: 0; */
}
</style>
