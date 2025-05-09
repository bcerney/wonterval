<script lang="ts">
    import { Progressbar } from "flowbite-svelte";

    let timeRemaining = 60;
    let totalTime = 60;
    let isRunning = false;
    let intervalId: number;
    
    $: progress = timeRemaining / totalTime;
    
    function startTimer() {
        if (isRunning) return;
        isRunning = true;
        intervalId = setInterval(() => {
            timeRemaining -= 1;
            if (timeRemaining <= 0) {
                stopTimer();
                timeRemaining = totalTime;
            }
        }, 1000);
    }
    
    function stopTimer() {
        clearInterval(intervalId);
        isRunning = false;
    }
    
    function resetTimer() {
        stopTimer();
        timeRemaining = totalTime;
    }
</script>

<h1>Session Details</h1>
<p>Test copy</p>

<div class="session-timer">
    <Progressbar progress=60 />
    <div class="time-display">
        {Math.floor(timeRemaining / 60)}:{(timeRemaining % 60).toString().padStart(2, '0')}
    </div>
    
    <div class="controls">
        <button on:click={startTimer} disabled={isRunning}>Start</button>
        <button on:click={stopTimer} disabled={!isRunning}>Stop</button>
        <button on:click={resetTimer}>Reset</button>
    </div>
</div>

<style>
    .session-timer {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2rem;
        padding: 2rem;
    }
    
    .time-display {
        font-size: 3rem;
        font-weight: bold;
    }
    
    .controls {
        display: flex;
        gap: 1rem;
    }
    
    button {
        padding: 0.5rem 1rem;
        font-size: 1.2rem;
        border-radius: 4px;
        border: none;
        background: #4CAF50;
        color: white;
        cursor: pointer;
    }
    
    button:disabled {
        background: #ccc;
        cursor: not-allowed;
    }
</style>