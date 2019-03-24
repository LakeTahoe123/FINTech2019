<template>
	<div class="home">
		<b-container fluid>
			<b-row>
				<b-col md="3">
					<b-row>
						<b-col style="padding: 20px;">
							<b-form-group id="salary" label="Expected Salary" label-for="salary">
								<b-form-input id="salary" v-model="salary" trim/>
							</b-form-group>

							<b-form-group id="searchbar" label="Search for Listings" label-for="searchbar">
								<b-form-input id="searchbar" v-model="location" trim/>
							</b-form-group>
						</b-col>
					</b-row>
				</b-col>
				<b-col>
					<div style="position: relative">
						<b-container fluid style=" padding-top:30px; padding-left:30px; padding-right: 30px;">
							<Listing/>
						</b-container>
					</div>
				</b-col>
			</b-row>
		</b-container>
	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Listing from "@/components/Listing.vue";

export default {
	name: "home",
	components: {
		HelloWorld,
		Listing
	},
	data() {
		return {
			location: "",
			salary: ""
		};
	}
};
</script>

<style>
/* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
#app #map {
	height: 100%;
}
</style>