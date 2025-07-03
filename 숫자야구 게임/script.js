
// 남은 시도 횟수 표시할 요소와 입력칸, 버튼, 결과 영역 가져오기
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

    clearInputs();
    resultsContainer.innerHTML = '';
    resultImage.src = '';
    resultImage.style.display = 'none';
    submitButton.disabled = false;
}

// 입력창 초기화해주는 함수
function clearInputs() {
    numberInputs.forEach(input => {
        input.value = '';
    });

    numberInputs[0].focus();
}

// 사용자가 숫자 3개 입력하고 확인 눌렀을 때 결과 계산해주는 함수
function check_numbers() {
    if (isGameOver) {
        return;
    }

    const userGuess = numberInputs.map(input => input.value);

    if (userGuess.some(num => num === '')) {
      
        clearInputs();
        return;
    }

    attempts--;
    attemptsDisplay.textContent = attempts;

    let strikes = 0;
    let balls = 0;
    const guessNumbers = userGuess.map(num => parseInt(num, 10));
    for (let i = 0; i < 3; i++) {
        if (guessNumbers[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(guessNumbers[i])) {
            balls++;
        }
    }

    const resultRow = document.createElement('div');
    resultRow.classList.add('check-result');

    const leftDiv = document.createElement('div');
    leftDiv.classList.add('left');
    leftDiv.textContent = `[ ${guessNumbers.join(', ')} ]`;

    const rightDiv = document.createElement('div');
    rightDiv.classList.add('right');

    let resultHTML = '';

    if (strikes === 0 && balls === 0) {
        // 아웃
        resultHTML = '<span class="num-result out">O</span>';
    } else {
        // 스트라이크
        if (strikes > 0) {
            resultHTML += `${strikes} <span class="num-result strike">S</span> `;
        }
        // 볼
        if (balls > 0) {
            resultHTML += `${balls} <span class="num-result ball">B</span>`;
        }
    }
    rightDiv.innerHTML = resultHTML.trim();

    resultRow.appendChild(leftDiv);
    resultRow.appendChild(rightDiv);
    resultsContainer.appendChild(resultRow);

    if (strikes === 3) {
        endGame(true);
    } else if (attempts <= 0) {
        endGame(false);
    } else {
        clearInputs();
    }
}
// 게임이 끝났을 때 이미지 보여주는 함
function endGame(isWin) {
    isGameOver = true;
    submitButton.disabled = true;
    resultImage.style.display = 'block';

    if (isWin) {
        resultImage.src = 'success.png';
    } else {
        resultImage.src = 'fail.png';
    }
}
// 숫자 입력시 자동 이동
numberInputs[0].addEventListener('input', () => {
    if (numberInputs[0].value.length === 1) numberInputs[1].focus();
});
numberInputs[1].addEventListener('input', () => {
    if (numberInputs[1].value.length === 1) numberInputs[2].focus();
});
numberInputs[2].addEventListener('input', () => {
    if (numberInputs[2].value.length === 1) submitButton.focus();
});
// 페이지 로딩시 게임 시작
initializeGame();