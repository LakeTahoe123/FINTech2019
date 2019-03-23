<template>
	<div class="listing">
		<b-container>
			<b-row no-gutters v-for="listing in listings" :key="listing.id">
				<b-col md="12">
					<b-card>
						<b-container fluid>
							<b-row>
								<b-col style="width:auto;">
									<img :src="listing.img_src" img-alt="Image" style="height: 200px; width: 300px;">
								</b-col>
								<b-col>
									<b-card-text>{{listing.description}}</b-card-text>
									<div slot="footer">
										<small class="text-muted">Last updated 3 mins ago</small>
									</div>
								</b-col>
							</b-row>
						</b-container>
					</b-card>
				</b-col>
			</b-row>
		</b-container>
	</div>
</template>

<script>
export default {
	data() {
		return {
			listings: [
				{
					id: 0,
					img_src: "https://placekitten.com/400/100",
					title: "Good Cat",
					description: "This is a good cat!"
				},
				{
					id: 1,
					img_src: "https://placekitten.com/600/150",
					title: "Great Cat",
					description: "This is a great cat!"
				},
				{
					id: 2,
					img_src: "https://placekitten.com/800/200",
					title: "Best Cat",
					description: "This is the best cat!"
				}
			]
		};
	}
};
</script>

<style>
</style>
