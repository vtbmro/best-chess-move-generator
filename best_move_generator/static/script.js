var draggable = document.getElementById("draggable1");

draggable.addEventListener('dragstart', dragStart, false);
draggable.addEventListener('dragend'  , dragEnd  , false);

var droptarget = document.getElementById("droptarget1");

droptarget.addEventListener('dragenter', dragEnter  , false);
droptarget.addEventListener('dragover' , dragOver   , false);
droptarget.addEventListener('dragleave', dragLeave  , false);
droptarget.addEventListener('drop'     , drop       , false);


/* Draggable event handlers */
function dragStart(event) {
    event.dataTransfer.setData('text/html', "You dragged the image!");
}

function dragEnd(event) {
}

/* Drop target event handlers */
function dragEnter(event) {
}

function dragOver(event) {
    event.preventDefault();
    return false;
}

function dragLeave(event) {
}

function drop(event) {
    var data = event.dataTransfer.getData('text/html');
    event.preventDefault();
    return false;
}

// TODO: allow click and drag of pieces that changes their position
// if dragged outside of board delete them

// TODO: clear board button

// TODO: start position button

// TODO: add outside sets of piece 