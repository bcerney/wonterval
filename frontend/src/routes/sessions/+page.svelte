<script lang="ts">
    let sessions = [
        { id: 1, name: "Workout 1", warmupTime: 300, timeBetweenSeries: 60 },
        { id: 2, name: "Workout 2", warmupTime: 180, timeBetweenSeries: 45 }
    ];
</script>

<h1>Sessions</h1>

<div class="sessions-list">
    {#each sessions as session}
        <a href="/sessions/{session.id}" class="session-card">
            <h2>{session.name}</h2>
            <p>Warmup: {session.warmupTime}s</p>
            <p>Rest between series: {session.timeBetweenSeries}s</p>
        </a>
    {/each}
</div>
<p>This is the Sessions page.</p>

<style>
    .sessions-list {
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        padding: 1rem;
    }

    .session-card {
        background: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        text-decoration: none;
        color: inherit;
    }

    .session-card:hover {
        background: #e0e0e0;
    }
</style>
