const attemptsDisplay = document.getElementById('attempts');
const numberInputs = [
    document.getElementById('number1'),
    document.getElementById('number2'),
    document.getElementById('number3')
];
const submitButton = document.querySelector('.submit-button');
const resultsContainer = document.getElementById('results');
const resultImage = document.getElementById('game-result-img');

let answer;
let attempts;
let isGameOver;

function initializeGame() {
    attempts = 9;
    isGameOver = false;
    attemptsDisplay.textContent = attempts;
    
    answer = [];
    const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    while (answer.length < 3) {
        const randomIndex = Math.floor(Math.random() * numbers.length);
        answer.push(numbers.splice(randomIndex, 1)[0]);
    }
    console.log('정답:', answer);

    clearInputs();
    resultsContainer.innerHTML = '';
    resultImage.src = '';
    resultImage.style.display = 'none';
    submitButton.disabled = false;
}

function clearInputs() {
    numberInputs.forEach(input => { input.value = ''; });
    numberInputs[0].focus();
}

function check_numbers() {
    if (isGameOver) return;

    const userGuess = numberInputs.map(input => parseInt(input.value, 10));
    if (userGuess.some(isNaN)) {
        alert('숫자 3개를 모두 입력해주세요.');
        return;
    }

    attempts--;
    attemptsDisplay.textContent = attempts;

    let strikes = 0;
    let balls = 0;
    for (let i = 0; i < 3; i++) {
        if (userGuess[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(userGuess[i])) {
            balls++;
        }
    }

    const resultDiv = document.createElement('div');
    resultDiv.textContent = `[${userGuess.join(', ')}] 결과: ${strikes}S ${balls}B`;
    resultsContainer.appendChild(resultDiv);

    if (strikes === 3) {
        endGame(true);
    } else if (attempts <= 0) {
        endGame(false);
    } else {
        clearInputs();
    }
}

function endGame(isWin) {
    isGameOver = true;
    submitButton.disabled = true;
    resultImage.style.display = 'block';
    resultImage.src = isWin ? 'success.png' : 'fail.png';
}

initializeGame();