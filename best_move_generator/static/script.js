// DOM loaded
document.addEventListener("DOMContentLoaded", function(){
    
    var board2 = Chessboard('board2', {
        draggable: true,
        dropOffBoard: 'trash',
        sparePieces: true
        })

        $('#startBtn').on('click', board2.start)
        $('#clearBtn').on('click', board2.clear)
        
    calculate_move()
})

// Function that transform the position in the UI into FEN value
function calculate_move(){

    // Get squares
    const board = document.querySelector(".board-b72b1")
    const rows = board.childNodes

    // Iterate trough rows 
    for (let i = 0; i < 8; i++){
        let row = rows[i].childNodes
        
        // Iterate trough square
        for(let k = 0; k < 8; k++){
            let square = row[k]

            
            
        }
        
    }
}