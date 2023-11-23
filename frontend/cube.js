let solutionBox = document.getElementById('solution');

function getColor(str){
    if(str=='R'){
        return 'red';
    }
    else if(str=='B'){
        return 'blue';
    }
    else if(str=='W'){
        return 'white';
    }
    else if(str=='Y'){
        return 'yellow';
    }
    else if(str=='G'){
        return 'green';
    }
    else if(str=='O'){
        return 'orange';
    }
}

let up=['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'];
let down=['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'];
let left=['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'];
let right=['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'];
let front=['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'];
let back=['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'];

let boxes=document.querySelectorAll('.box');
function display(){
    boxes[0].style.backgroundColor=getColor(up[0]);
    boxes[1].style.backgroundColor=getColor(up[1]);
    boxes[2].style.backgroundColor=getColor(up[2]);
    boxes[3].style.backgroundColor=getColor(up[3]);
    boxes[4].style.backgroundColor=getColor(up[4]);
    boxes[5].style.backgroundColor=getColor(up[5]);
    boxes[6].style.backgroundColor=getColor(up[6]);
    boxes[7].style.backgroundColor=getColor(up[7]);
    boxes[8].style.backgroundColor=getColor(up[8]);
    boxes[9].style.backgroundColor=getColor(left[0]);
    boxes[10].style.backgroundColor=getColor(left[1]);
    boxes[11].style.backgroundColor=getColor(left[2]);
    boxes[12].style.backgroundColor=getColor(left[3]);
    boxes[13].style.backgroundColor=getColor(left[4]);
    boxes[14].style.backgroundColor=getColor(left[5]);
    boxes[15].style.backgroundColor=getColor(left[6]);
    boxes[16].style.backgroundColor=getColor(left[7]);
    boxes[17].style.backgroundColor=getColor(left[8]);
    boxes[18].style.backgroundColor=getColor(front[0]);
    boxes[19].style.backgroundColor=getColor(front[1]);
    boxes[20].style.backgroundColor=getColor(front[2]);
    boxes[21].style.backgroundColor=getColor(front[3]);
    boxes[22].style.backgroundColor=getColor(front[4]);
    boxes[23].style.backgroundColor=getColor(front[5]);
    boxes[24].style.backgroundColor=getColor(front[6]);
    boxes[25].style.backgroundColor=getColor(front[7]);
    boxes[26].style.backgroundColor=getColor(front[8]);
    boxes[27].style.backgroundColor=getColor(right[0]);
    boxes[28].style.backgroundColor=getColor(right[1]);
    boxes[29].style.backgroundColor=getColor(right[2]);
    boxes[30].style.backgroundColor=getColor(right[3]);
    boxes[31].style.backgroundColor=getColor(right[4]);
    boxes[32].style.backgroundColor=getColor(right[5]);
    boxes[33].style.backgroundColor=getColor(right[6]);
    boxes[34].style.backgroundColor=getColor(right[7]);
    boxes[35].style.backgroundColor=getColor(right[8]);
    boxes[36].style.backgroundColor=getColor(back[0]);
    boxes[37].style.backgroundColor=getColor(back[1]);
    boxes[38].style.backgroundColor=getColor(back[2]);
    boxes[39].style.backgroundColor=getColor(back[3]);
    boxes[40].style.backgroundColor=getColor(back[4]);
    boxes[41].style.backgroundColor=getColor(back[5]);
    boxes[42].style.backgroundColor=getColor(back[6]);
    boxes[43].style.backgroundColor=getColor(back[7]);
    boxes[44].style.backgroundColor=getColor(back[8]);
    boxes[45].style.backgroundColor=getColor(down[0]);
    boxes[46].style.backgroundColor=getColor(down[1]);
    boxes[47].style.backgroundColor=getColor(down[2]);
    boxes[48].style.backgroundColor=getColor(down[3]);
    boxes[49].style.backgroundColor=getColor(down[4]);
    boxes[50].style.backgroundColor=getColor(down[5]);
    boxes[51].style.backgroundColor=getColor(down[6]);
    boxes[52].style.backgroundColor=getColor(down[7]);
    boxes[53].style.backgroundColor=getColor(down[8]);
}
setInterval(display,1);

function addEvents(btn,str){
    btn.addEventListener('click',()=>{
        boxes[0].addEventListener('click', () => {up[0]=str;});
        boxes[1].addEventListener('click', () => {up[1]=str;});
        boxes[2].addEventListener('click', () => {up[2]=str;});
        boxes[3].addEventListener('click', () => {up[3]=str;});
        boxes[4].addEventListener('click', () => {up[4]=str;});
        boxes[5].addEventListener('click', () => {up[5]=str;});
        boxes[6].addEventListener('click', () => {up[6]=str;});
        boxes[7].addEventListener('click', () => {up[7]=str;});
        boxes[8].addEventListener('click', () => {up[8]=str;});
        boxes[9].addEventListener('click', () => {left[0]=str;});
        boxes[10].addEventListener('click', () => {left[1]=str;});
        boxes[11].addEventListener('click', () => {left[2]=str;});
        boxes[12].addEventListener('click', () => {left[3]=str;});
        boxes[13].addEventListener('click', () => {left[4]=str;});
        boxes[14].addEventListener('click', () => {left[5]=str;});
        boxes[15].addEventListener('click', () => {left[6]=str;});
        boxes[16].addEventListener('click', () => {left[7]=str;});
        boxes[17].addEventListener('click', () => {left[8]=str;});
        boxes[18].addEventListener('click', () => {front[0]=str;});
        boxes[19].addEventListener('click', () => {front[1]=str;});
        boxes[20].addEventListener('click', () => {front[2]=str;});
        boxes[21].addEventListener('click', () => {front[3]=str;});
        boxes[22].addEventListener('click', () => {front[4]=str;});
        boxes[23].addEventListener('click', () => {front[5]=str;});
        boxes[24].addEventListener('click', () => {front[6]=str;});
        boxes[25].addEventListener('click', () => {front[7]=str;});
        boxes[26].addEventListener('click', () => {front[8]=str;});
        boxes[27].addEventListener('click', () => {right[0]=str;});
        boxes[28].addEventListener('click', () => {right[1]=str;});
        boxes[29].addEventListener('click', () => {right[2]=str;});
        boxes[30].addEventListener('click', () => {right[3]=str;});
        boxes[31].addEventListener('click', () => {right[4]=str;});
        boxes[32].addEventListener('click', () => {right[5]=str;});
        boxes[33].addEventListener('click', () => {right[6]=str;});
        boxes[34].addEventListener('click', () => {right[7]=str;});
        boxes[35].addEventListener('click', () => {right[8]=str;});
        boxes[36].addEventListener('click', () => {back[0]=str;});
        boxes[37].addEventListener('click', () => {back[1]=str;});
        boxes[38].addEventListener('click', () => {back[2]=str;});
        boxes[39].addEventListener('click', () => {back[3]=str;});
        boxes[40].addEventListener('click', () => {back[4]=str;});
        boxes[41].addEventListener('click', () => {back[5]=str;});
        boxes[42].addEventListener('click', () => {back[6]=str;});
        boxes[43].addEventListener('click', () => {back[7]=str;});
        boxes[44].addEventListener('click', () => {back[8]=str;});
        boxes[45].addEventListener('click', () => {down[0]=str;});
        boxes[46].addEventListener('click', () => {down[1]=str;});
        boxes[47].addEventListener('click', () => {down[2]=str;});
        boxes[48].addEventListener('click', () => {down[3]=str;});
        boxes[49].addEventListener('click', () => {down[4]=str;});
        boxes[50].addEventListener('click', () => {down[5]=str;});
        boxes[51].addEventListener('click', () => {down[6]=str;});
        boxes[52].addEventListener('click', () => {down[7]=str;});
        boxes[53].addEventListener('click', () => {down[8]=str;});
    });
}
let redBtn=document.getElementById('t1');
let whiteBtn=document.getElementById('t2');
let yellowBtn=document.getElementById('t3');
let orangeBtn=document.getElementById('t4');
let greenBtn=document.getElementById('t5');
let blueBtn=document.getElementById('t6');
addEvents(redBtn,'R');
addEvents(whiteBtn,'W');
addEvents(blueBtn,'B');
addEvents(orangeBtn,'O');
addEvents(greenBtn,'G');
addEvents(yellowBtn,'Y');

let resetbtn = document.getElementById('reset');
resetbtn.addEventListener('click', () => {
    up=['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'];
    down=['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'];
    left=['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'];
    right=['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'];
    front=['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'];
    back=['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'];
    solutionBox.innerHTML = "Solution appears here...";
});

function mapper(character){
    if(character == 'W'){
        return 'U'
    }
    else if(character == 'Y'){
        return 'D'
    }
    else if(character == 'R'){
        return 'R'
    }
    else if(character == 'O'){
        return 'L'
    }
    else if(character == 'B'){
        return 'B'
    }
    else{
        return 'F'
    }
}
let solvebtn = document.getElementById('solve');
solvebtn.addEventListener('click', () => {
    cubeStr = "";
    for(char in up){
        cubeStr += mapper(up[char]);
    }
    for(char in right){
        cubeStr += mapper(right[char]);
    }
    for(char in front){
        cubeStr += mapper(front[char]);
    }
    for(char in down){
        cubeStr += mapper(down[char]);
    }
    for(char in left){
        cubeStr += mapper(left[char]);
    }
    for(char in back){
        cubeStr += mapper(back[char]);
    }
    
    const data = {
        cubeStr: cubeStr
    };
    
    fetch('http://127.0.0.1:8000/api/solvecube', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if(data.message != "Entered configuration is invalid or out of limit!!"){
            up=['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'];
            down=['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'];
            left=['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'];
            right=['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'];
            front=['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'];
            back=['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'];
        }
        solutionBox.innerHTML = data.message;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });

});