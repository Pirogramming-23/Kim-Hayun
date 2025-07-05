const stopwatchDisplay = document.getElementById('stopwatch-display');
const startStopBtn = document.getElementById('start-stop-btn');

const resetBtn = document.getElementById('reset-btn');

const recordBtn = document.getElementById('record-btn');
const recordList = document.getElementById('record-list');
const selectAllBtn = document.getElementById('select-all-btn');
const deleteSelectedBtn = document.getElementById('delete-selected-btn');

const stopwatchTab = document.getElementById('stopwatch-tab');
const timerTab = document.getElementById('timer-tab');
const stopwatchSection = document.getElementById('stopwatch-section');
const timerSection = document.getElementById('timer-section');

const timerDisplay = document.getElementById('timer-display');
const startTimerBtn = document.getElementById('start-timer-btn');
const resetTimerBtn = document.getElementById('reset-timer-btn');
const hoursInput = document.getElementById('hours');
const minutesInput = document.getElementById('minutes');
const secondsInput = document.getElementById('seconds');

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

resetBtn.addEventListener('click',()=>{
  clearInterval(stopwatchInterval);
  isRunning=false;
  elapsedTime=0;
  stopwatchDisplay.textContent="00:00:00";
  startStopBtn.textContent="start";
})

recordBtn.addEventListener('click', () => {
 if (elapsedTime === 0) return; 

  const li =document.createElement('li');
  const currentTime = formatTime(elapsedTime);
  li.className='record-item';
  li.innerHTML = `
  <input type="checkbox" class="record-checkbox">
  <span class="record-text">${currentTime}</span>
  <button class="delete-record-btn">🗑️</button>
  `;
  li.querySelector('.delete-record-btn').addEventListener('click', (e) => {
    e.target.closest('.record-item').remove();
  });
  recordList.prepend(li);
});

selectAllBtn.addEventListener('click', () => {
  const checkboxes = document.querySelectorAll('.record-checkbox');
  const allChecked = checkboxes.length > 0 && Array.from(checkboxes).every(cb => cb.checked);
  checkboxes.forEach(cb => cb.checked = !allChecked);
});

deleteSelectedBtn.addEventListener('click', () => {
  const checked = document.querySelectorAll('.record-checkbox:checked');
  checked.forEach(cb => {
    cb.closest('.record-item').remove();
  });
});


stopwatchTab.addEventListener('click', () => {
  stopwatchTab.classList.add('active');
  timerTab.classList.remove('active');
  stopwatchSection.classList.add('active');
  timerSection.classList.remove('active');
});

timerTab.addEventListener('click', () => {
  timerTab.classList.add('active');
  stopwatchTab.classList.remove('active');
  timerSection.classList.add('active');
  stopwatchSection.classList.remove('active');
});

let timerInterval;
let totalSeconds = 0;
let isTimerRunning = false;

function formatTimerTime(sec) {
  const h = String(Math.floor(sec / 3600)).padStart(2, '0');
  const m = String(Math.floor((sec % 3600) / 60)).padStart(2, '0');
  const s = String(sec % 60).padStart(2, '0');
  return `${h}:${m}:${s}`;
}

startTimerBtn.addEventListener('click', () => {
  if (isTimerRunning) {
    clearInterval(timerInterval);
    isTimerRunning = false;
    startTimerBtn.textContent = 'resume';
    return;
  }

  if (totalSeconds <= 0) {
    const h = parseInt(hoursInput.value) || 0;
    const m = parseInt(minutesInput.value) || 0;
    const s = parseInt(secondsInput.value) || 0;
    totalSeconds = h * 3600 + m * 60 + s;
  }

  if (totalSeconds > 0) {
    isTimerRunning = true;
    startTimerBtn.textContent = 'pause';
    timerInterval = setInterval(() => {
      totalSeconds--;
      timerDisplay.textContent = formatTimerTime(totalSeconds);
      if (totalSeconds <= 0) {
        clearInterval(timerInterval);
        isTimerRunning = false;
        startTimerBtn.textContent = 'start';
        timerDisplay.textContent = "Times  Up!";
      }
    }, 1000);
  }
});

resetTimerBtn.addEventListener('click', () => {
  clearInterval(timerInterval);
  isTimerRunning = false;
  totalSeconds = 0;
  hoursInput.value = '';
  minutesInput.value = '';
  secondsInput.value = '';
  timerDisplay.textContent = '00:00:00';
  startTimerBtn.textContent = 'start';
});