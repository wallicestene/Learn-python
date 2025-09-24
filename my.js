function solution(board) {
    const rows = board.length
    const cols = board[0].length

    // Convert strings to arrays if needed
    const matrix = board.map(row =>
        typeof row === 'string' ? row.split('') : [...row]
    );

    // Step 1: Apply gravity - make boxes fall
    for (let col = 0; col < cols; col++) {
        let writeRow = rows - 1

        for (let row = rows - 1; row >= 0; row--) {
            const cell = matrix[row][col]

            if (cell === "*") {
                // Obstacle blocks further falling
                writeRow = row - 1
            } else if (cell === "#") {
                // Box falls to writeRow position
                if (writeRow !== row) {
                    matrix[writeRow][col] = "#"
                    matrix[row][col] = "-"
                }
                writeRow--
            }
        }

        // Fill remaining positions above with empty cells
        for (let fill = writeRow; fill >= 0; fill--) {
            if (matrix[fill][col] !== "*") {
                matrix[fill][col] = "-"
            }
        }
    }

    // Step 2: Handle explosions
    const explosions = new Set()

    // Find all obstacles and check for boxes that would explode
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (matrix[row][col] === "*") {
                // Check 8 surrounding cells for boxes
                for (let dr = -1; dr <= 1; dr++) {
                    for (let dc = -1; dc <= 1; dc++) {
                        if (dr === 0 && dc === 0) continue // Skip the obstacle itself

                        const newRow = row + dr
                        const newCol = col + dc

                        if (newRow >= 0 && newRow < rows &&
                            newCol >= 0 && newCol < cols &&
                            matrix[newRow][newCol] === "#") {
                            // Mark this box for explosion
                            explosions.add(`${newRow},${newCol}`)
                        }
                    }
                }
            }
        }
    }

    // Remove exploded boxes
    for (const explosion of explosions) {
        const [row, col] = explosion.split(',').map(Number)
        matrix[row][col] = "-"
    }

    // Return in the same format as input
    return typeof board[0] === 'string'
        ? matrix.map(row => row.join(''))
        : matrix
}
// Example usage
const board = [
    ['-', '-', '*', '-', '#'],
    ['-', '#', '-', '*', '-'],
    ['#', '-', '-', '-', '-'],
    ['-', '*', '-', '#', '-'],
    ['-', '-', '-', '-', '-']
];
// console.log(solution(board));

