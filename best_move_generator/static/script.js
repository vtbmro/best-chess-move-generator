// DOM loaded
document.addEventListener("DOMContentLoaded", function(){
    
    var board2 = Chessboard('board2', {
        draggable: true,
        dropOffBoard: 'trash',
        sparePieces: true
        })

        $('#startBtn').on('click', board2.start)
        $('#clearBtn').on('click', board2.clear)
        
    let main_button = document.querySelector("#calculateBtn")
    main_button.addEventListener("click", function(){
        get_fen_notation()
    })
})

// Function that transform the position in the UI into FEN value
function get_fen_notation(){

    // Get squares
    const board = document.querySelector(".board-b72b1")
    const rows = board.childNodes
    
    // Define FEN
    let fen = ""

    // Iterate trough rows 
    for (let i = 0; i < 8; i++){
        let row = rows[i].childNodes
        let counter = 0

        // Iterate trough square
        for(let k = 0; k < 8; k++){

            let square = row[k]
            
            // If div is empty (no img inside add 1 to counter)
            if (square.getElementsByTagName('img').length > 0){

                let img = square.getElementsByTagName('img')

                if(counter != 0){
                    fen += counter.toString();
                    counter = 0
                }

                // Add corresponding piece
                switch (img[0].getAttribute("data-piece")){

                    // Black
                    case "bR":
                        fen += "r"
                        break;
                    case "bN":
                        fen += "n"
                        break;
                    case "bB":
                        fen += "b"
                        break;
                    case "bQ":
                            fen += "q"
                        break;  
                    case "bK":
                        fen += "k"
                        break;
                    case "bP":
                        fen += "p"

                    // White 
                        break;
                    case "wR":
                        fen += "R"
                        break;
                    case "wN":
                        fen += "N"
                        break;
                    case "wB":
                        fen += "B"
                        break;
                    case "wQ":
                        fen += "Q"
                        break;  
                    case "wK":
                        fen += "K"
                        break;
                    case "wP":
                        fen += "P"
                        break;                     
                }               
            }else if(square.getElementsByTagName('img').length == 0){
                counter += 1
            }
            
            // End of the row
            if(k == 7)
            {   
                if(counter != 0)
                {
                  fen += counter.toString();
                    counter = 0  
                }
            
                fen += "/"
            }
        }   
    }
    
    console.log(fen.slice(0,-1))


    // NOTE: could have used something more complex but this does the trick
}