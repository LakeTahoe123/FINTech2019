<template>
	<div class="home">
		<b-container fluid>
			<b-row>
				<b-col md="3">
					<b-row>
						<b-col style="padding: 20px;">
							<h1>
								I made this
								<b>Vue</b> App
							</h1>

							<b-form-group
								id="searchbar"
								description="Search for Listings"
								label="Search for Listings"
								label-for="searchbar"
							>
								<b-form-input id="searchbar" v-model="name" trim/>
							</b-form-group>
							{{name}}
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
			name: ""
		};
	}
};
</script>
