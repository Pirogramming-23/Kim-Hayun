const stopwatchDisplay = document.getElementById('stopwatch-display');
const startStopBtn = document.getElementById('start-stop-btn');

let isRunning = false;
let startTime = 0;
let elapsedTime = 0;
let stopwatchInterval;

function formatTime(ms) {
  const totalSec = Math.floor(ms / 1000);
  const min = String(Math.floor(totalSec / 60)).padStart(2, '0');
  const sec = String(totalSec % 60).padStart(2, '0');
  const ms2 = String(Math.floor((ms % 1000) / 10)).padStart(2, '0');
  return `${min}:${sec}:${ms2}`;
}

startStopBtn.addEventListener('click', () => {
  if (!isRunning) {
    startTime = Date.now() - elapsedTime;
    stopwatchInterval = setInterval(() => {
      elapsedTime = Date.now() - startTime;
      stopwatchDisplay.textContent = formatTime(elapsedTime);
    }, 10);
    startStopBtn.textContent = 'stop';
    isRunning = true;
  } else {
    clearInterval(stopwatchInterval);
    startStopBtn.textContent = 'start';
    isRunning = false;
  }
})