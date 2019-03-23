<template>
	<b-navbar fluid toggleable="md" type="dark" variant="info">
		<b-navbar-brand :to="{ name: 'Home' }">Account-Owner Home</b-navbar-brand>
		<b-navbar-nav>
			<b-nav-item to="/">Home</b-nav-item>
			<b-nav-item to="/about">About</b-nav-item>
		</b-navbar-nav>
	</b-navbar>
</template>
<script>
export default {
	name: "Navbar"
};
</script>