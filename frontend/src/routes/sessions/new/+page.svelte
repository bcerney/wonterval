<script>
    import { Input, Label, Helper, Button, Checkbox, A } from "flowbite-svelte";

    let sessionName = '';
    let warmupTime = 0;
    let timeBetweenSeries = 0;
    let repIndicator = 'sound';
    let series = [{
        activity: '',
        cadence: 0,
        setTime: 0,
        restAfterSet: 0,
        numberOfSets: 0
    }];

    function addSeries() {
        series = [...series, {
            activity: '',
            cadence: 0,
            setTime: 0,
            restAfterSet: 0,
            numberOfSets: 0
        }];
    }

    function removeSeries(index) {
        series = series.filter((_, i) => i !== index);
    }

    function handleSubmit() {
        // TODO: Handle form submission
        console.log({ sessionName, warmupTime, timeBetweenSeries, repIndicator, series });

    }
</script>

<div>
    <h1>New Session</h1>

    <form on:submit|preventDefault={handleSubmit}>
        <div class="mb-6 grid gap-6 md:grid-cols-2">
            <div>
                <Label for="sessionName">Session Name:</Label>
                <Input id="sessionName" bind:value={sessionName} required/>
            </div>
        
            <div>
                <Label for="warmupTime">Warmup Time (seconds):</Label>
                <Input id="warmupTime" type="number" bind:value={warmupTime} min="0" required/>
            </div>
        
            <div>
                <Label for="timeBetweenSeries">Time Between Series (seconds):</Label>
                <Input id="timeBetweenSeries" type="number" bind:value={timeBetweenSeries} min="0" required/>
            </div>
        
            <div>
                <Label for="repIndicator">Rep Indicator:</Label>
                <select id="repIndicator" bind:value={repIndicator}>
                    <option value="sound">Sound</option>
                    <option value="lights">Lights</option>
                </select>
            </div>
        
            <h2>Series</h2>
            {#each series as serie, i}
                <fieldset>
                    <legend>Series {i + 1}</legend>
                    <div>
                        <Label for="activity{i}">Activity:</Label>
                        <Input id="activity{i}" bind:value={serie.activity} required/>
                    </div>
                    <div>
                        <Label for="cadence{i}">Cadence (reps/min):</Label>
                        <Input id="cadence{i}" type="number" bind:value={serie.cadence} min="0" required/>
                    </div>
                    <div>
                        <Label for="setTime{i}">Set Time (seconds):</Label>
                        <Input id="setTime{i}" type="number" bind:value={serie.setTime} min="0" required/>
                    </div>
                    <div>
                        <Label for="restAfterSet{i}">Rest After Set (seconds):</Label>
                        <Input id="restAfterSet{i}" type="number" bind:value={serie.restAfterSet} min="0" required/>
                    </div>
                    <div>
                        <Label for="numberOfSets{i}">Number of Sets:</Label>
                        <Input id="numberOfSets{i}" type="number" bind:value={serie.numberOfSets} min="1" required/>
                    </div>
                    {#if series.length > 1}
                        <button type="button" on:click={() => removeSeries(i)}>Remove Series</button>
                    {/if}
                </fieldset>
            {/each}
        </div>

    
        <button type="button" on:click={addSeries}>Add Series</button>
        <button type="submit">Create Session</button>
    </form>    

</div>


<style>
    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    
    fieldset {
        border: 1px solid #ccc;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    div {
        margin-bottom: 0.5rem;
    }
    
    Label {
        display: block;
        margin-bottom: 0.25rem;
    }
</style>
