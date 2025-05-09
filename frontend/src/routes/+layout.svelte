<script lang="ts">
	import '../app.css';

	let { children } = $props();
</script>

<nav>
	<a href="/">Home</a>
	<a href="/sessions/new">New Session</a>
	<a href="/sessions">Sessions</a>
</nav>

{@render children()}
