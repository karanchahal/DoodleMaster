//hey
var count = -1;
var flag = false; 

// Function to show the modal for ID of the new view
function showModal(){
    $('#exampleModal').modal('show');
    $('#exampleModal').on('shown.bs.modal', function () {
        $('#element-name').trigger('focus')
    })
}

function hideModal(){
    $('#exampleModal').modal('hide');
    $('body').removeClass('modal-open')
    $('.modal-backdrop').remove()
}

function addElement(element_name){
    //showModal();
    count++;
    let blinkingCursor = document.getElementById("blinking-cursor");
    let predictedClass = document.getElementById("predicted-class");
    let colors = ['red', 'green', 'yellow', 'purple', 'orange', 'blue', 'indigo', 'teal']
    let text_colors = ['white','white','black','white','black','white','white','white']
    let div = document.getElementById('elements');
    div.innerHTML += '<div class="row"><div id="circle" style="background-color:' + colors[count%8] + '; margin-left:1vw ; color: '+ text_colors[count%8] +'">'+element_name.charAt(0) +'</div><p id="element-name"> - ' +element_name+ '</p></div>';
    predictedClass.innerHTML = element_name;
    blinkingCursor.style.display = 'none';
    predictedClass.style.display = 'block';
}

function savedId(){
    let id = document.getElementById("element-id").value
    hideModal()
    return id
    // Call here the pthon script
}

function changeAspectRatio(){
    let canvas = document.getElementById('drawingboard');
    let canvas_wrapper = document.getElementsByClassName("drawing-board-canvas-wrapper")[0];
    let drawingboard = document.getElementsByClassName("drawing-board-canvas")[0];
    if (flag){
        canvas.style.width = 'calc((9/16)*75vh)';
         flag = false;
    }else{
        canvas.style.width = 'calc((3/4)*75vh)';
        flag = true;
    }

    myBoard = new DrawingBoard.Board('drawingboard',{
        controls: false,
        color: '#000',
        size: 10,
        background: '#fff',
	    webStorage: true,
        enlargeYourContainer: true
      })

}

// Drawing board code here


//function post

function post(path,doodleData) {
    var method = "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var params = {"doodle":doodleData,"coords":[min_x,min_y,max_x,max_y]};
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit( function(e) {
    e.preventDefault()
    });
}

//global variables

let flag2= 0
let max_x = 0, max_y = 0,min_x = 100000,min_y = 1000000
let flag3 = 0

const socket = io('http://localhost:5000/');
let undo_stack = []

socket.on('message', function(payload) {
    console.log(payload.message)
    let predicted = payload.message
    addElement(predicted)
})
    
let myflag = 0
let myBoard = new DrawingBoard.Board('drawingboard',{
    controls: false,
    color: '#000',
    size: 6,
    background: '#fff',
    webStorage: true,
    enlargeYourContainer: true
})

     
myBoard.ev.bind('board:stopDrawing', function() {
//console.log('stop')
    myflag = 0
});

myBoard.ev.bind('board:startDrawing', function() {
//console.log('start')
    myflag = 1
});


myBoard.ev.bind('board:mouseOver', function() {
//console.log('start')
    flag3 = 1
});

myBoard.ev.bind('board:mouseOut', function() {
//console.log('start')
    flag3 = 0
});


myBoard.ev.bind('board:drawing', function(event) {

    if(myflag == 1 ) {
        //console.log('Drawing')
        //console.log(event.coords)
        let x = event.coords.x
        let y = event.coords.y
        if(x < min_x) {
        min_x = x
        }

        if(x > max_x) {
        max_x = x
        }

        if(y < min_y) {
        min_y = y
        }

        if(y > max_y) {
        max_y = y
        }
    }
});

myBoard.ev.bind('board:mouseOver', function(event) {
    
    
});


addEventListener('keypress',saveImage);


function saveImage(e) {    
    var key = e.which || e.keyCode;
    if (key === 13) { // 13 is enter
        console.log('Inside enter condition... Enter Pressed!!')
        showModal()
    }
}


function savedMyID() {
    

    console.log('saved button clicked.');
    //console.log(min_x,min_y,max_x,max_y)
    myBoard.getImg()
    var img = myBoard.getImg();
    //we keep drawingboard content only if it's not the 'blank canvas'
    var imgInput = (myBoard.blankCanvas == img) ? '' : img;
    
    // $.ajax({
    //   type: "POST",
    //   url: url,
    //   data: {"doodle":"dcdc","coords":[1,2,3,4]},
    //   success: function(res) {
    //     console.log(res)
    //   }
    // });

    
    id = savedId()
    console.log('whats up')
    socket.emit('getImg',{'doodle':imgInput,'id':String(id),'coords':[min_x,min_y,max_x,max_y]})
    undo_stack.push([min_x,min_y,max_x,max_y])
    //console.log(undo_stack)
    max_x = 0
    max_y = 0
    min_x = 100000
    min_y = 1000000
    //myBoard.reset({background:!0})

}

function reset() {
    socket.emit('clear',{})
    window.location.reload()  
}
