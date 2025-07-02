let answer;


function initializeGameLogic() {
    answer = [];
    const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    while (answer.length < 3) {
        const randomIndex = Math.floor(Math.random() * numbers.length);
        answer.push(numbers.splice(randomIndex, 1)[0]);
    }
    console.log('정답:', answer); 
}

function calculateResult(guess) {
    let strikes = 0;
    let balls = 0;
    for (let i = 0; i < 3; i++) {
        if (guess[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(guess[i])) {
            balls++;
        }
    }
    return { strikes, balls };
}

initializeGameLogic();