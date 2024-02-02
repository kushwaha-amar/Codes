let currentPlayer = "X";
let gameActive = true;
let moves = 0;
let player1Score = 0;
let player2Score = 0;

const cells = document.querySelectorAll("td");
const message = document.getElementById("message");
const player1ScoreDisplay = document.getElementById("player1Score");
const player2ScoreDisplay = document.getElementById("player2Score");
const resetButton = document.getElementById("resetButton");

const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function handleCellClick(e) {
    const clickedCell = e.target;

    if (clickedCell.textContent === "" && gameActive) {
        clickedCell.textContent = currentPlayer;
        moves++;
        checkResult();

        currentPlayer = currentPlayer === "X" ? "O" : "X";
    }
}

function checkResult() {
    for (let i = 0; i < winningCombinations.length; i++) {
        const [a, b, c] = winningCombinations[i];

        const cellA = cells[a].textContent;
        const cellB = cells[b].textContent;
        const cellC = cells[c].textContent;

        if (cellA !== "" && cellA === cellB && cellB === cellC) {
            gameActive = false;
            highlightWinningCells([a, b, c]);

            if (currentPlayer === "X") {
                player2Score++;
                message.textContent = "Player 2 (O) wins!";
            } else {
                player1Score++;
                message.textContent = "Player 1 (X) wins!";
            }

            updateScoreboard();
            setTimeout(resetGame, 1500);
            break;
        } else if (moves === 9) {
            gameActive = false;
            message.textContent = "It's a draw!";
            updateScoreboard();
            setTimeout(resetGame, 1500);
            break;
        }
    }
}

function highlightWinningCells(cellsToHighlight) {
    for (let i = 0; i < cellsToHighlight.length; i++) {
        cells[cellsToHighlight[i]].classList.add("winner");
    }
}

function updateScoreboard() {
    player1ScoreDisplay.textContent = "Player 1 (X): " + player1Score;
    player2ScoreDisplay.textContent = "Player 2 (O): " + player2Score;
}

function resetGame() {
    gameActive = true;
    moves = 0;
    message.textContent = "";
    cells.forEach(cell => {
        cell.textContent = "";
        cell.classList.remove("winner");
    });
}

resetButton.addEventListener("click", function() {
    resetGame();
    player1Score = 0;
    player2Score = 0;
    updateScoreboard();
});

cells.forEach(cell => {
    cell.addEventListener("click", handleCellClick);
});
