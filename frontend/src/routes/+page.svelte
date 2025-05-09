<script>
  import { Input, Label, Helper, Button, Checkbox, A } from "flowbite-svelte";

  

  let sessionName = '';
  let warmupTimeHours = 0;
  let warmupTimeMinutes = 0;
  let warmupTimeSeconds = 0;
  let timeBetweenSeriesHours = 0;
  let timeBetweenSeriesMinutes = 0;
  let timeBetweenSeriesSeconds = 0;
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

<div class="p-8">
  <h1>New Session</h1>

  <form on:submit|preventDefault={handleSubmit}>
      <div class="p-8 mb-6 grid gap-6 md:grid-cols-3">
          <div>
              <Label for="sessionName">Session Name:</Label>
              <Input id="sessionName" bind:value={sessionName} required/>
          </div>
      
          <div>
              <Label for="warmupTime">Warmup Time (seconds):</Label>
              <Input id="warmupTime" type="number" bind:value={warmupTime} min="0" required/>
          </div>
      
            <div class="space-y-2">
              <Label for="timeBetweenSeries">Time Between Series:</Label>
              <div class="flex gap-2">
                <div>
                  <Input id="timeBetweenSeriesHours" type="number" 
                    bind:value={Math.floor(timeBetweenSeries / 3600)} 
                    on:input={(e) => timeBetweenSeries = (parseInt(e.target.value) || 0) * 3600 + (timeBetweenSeries % 3600)}
                    min="0" placeholder="Hours"/>
                  <Helper>Hours</Helper>
                </div>
                <div>
                  <Input id="timeBetweenSeriesMinutes" type="number" 
                    bind:value={Math.floor((timeBetweenSeries % 3600) / 60)}
                    on:input={(e) => timeBetweenSeries = Math.floor(timeBetweenSeries / 3600) * 3600 + (parseInt(e.target.value) || 0) * 60 + (timeBetweenSeries % 60)}
                    min="0" max="59" placeholder="Minutes"/>
                  <Helper>Minutes</Helper>
                </div>
                <div>
                  <Input id="timeBetweenSeriesSeconds" type="number" 
                    bind:value={timeBetweenSeries % 60}
                    on:input={(e) => timeBetweenSeries = Math.floor(timeBetweenSeries / 60) * 60 + (parseInt(e.target.value) || 0)}
                    min="0" max="59" placeholder="Seconds"/>
                  <Helper>Seconds</Helper>
                </div>
              </div>
            </div>
      </div>
          <h2>Series</h2>
          {#each series as seriez, i}
              <fieldset>
                  <legend>Series {i + 1}</legend>
                  <div>
                      <Label for="activity{i}">Activity:</Label>
                      <Input id="activity{i}" bind:value={seriez.activity} required/>
                  </div>
                  <div>
                      <Label for="cadence{i}">Cadence (reps/min):</Label>
                      <Input id="cadence{i}" type="number" bind:value={seriez.cadence} min="0" required/>
                  </div>
                  <div>
                      <Label for="setTime{i}">Set Time (seconds):</Label>
                      <Input id="setTime{i}" type="number" bind:value={seriez.setTime} min="0" required/>
                  </div>
                  <div>
                      <Label for="restAfterSet{i}">Rest After Set (seconds):</Label>
                      <Input id="restAfterSet{i}" type="number" bind:value={seriez.restAfterSet} min="0" required/>
                  </div>
                  <div>
                      <Label for="numberOfSets{i}">Number of Sets:</Label>
                      <Input id="numberOfSets{i}" type="number" bind:value={seriez.numberOfSets} min="1" required/>
                  </div>
                  {#if series.length > 1}
                      <Button type="button" onclick={() => removeSeries(i)}>Remove Series</Button>
                  {/if}
              </fieldset>
          {/each}
      </div>

  
      <Button type="button" onclick={addSeries}>Add Series</Button>
      <Button type="submit">Create Session</Button>
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
