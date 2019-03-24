<template>
	<b-navbar fill toggleable="md" type="dark" variant="custom" style="background-color: #2C3840">
		<b-navbar-nav>
			<b-nav-item to="/">Home</b-nav-item>
		</b-navbar-nav>

		<b-navbar-nav class="ml-auto">
			<b-nav-text right>
				<a href="#">Sign in</a> to Save
			</b-nav-text>
		</b-navbar-nav>
	</b-navbar>
</template>
<script>
export default {
	name: "Navbar"
};
</script>