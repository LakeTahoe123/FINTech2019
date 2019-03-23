<template>
	<b-navbar fill toggleable="md" type="dark" variant="primary">
		<b-navbar-brand :to="{ name: 'Home' }">Account-Owner Home</b-navbar-brand>

		<b-navbar-nav>
			<b-nav-item to="/">Home</b-nav-item>
			<b-nav-item to="/about">About</b-nav-item>
		</b-navbar-nav>

		<b-navbar-nav class="ml-auto">
			<b-nav-text right>Sign in to Save</b-nav-text>
		</b-navbar-nav>
	</b-navbar>
</template>
<script>
export default {
	name: "Navbar"
};
</script>