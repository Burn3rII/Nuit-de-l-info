
// Konami code

const code=["Up","Up","Down","Down","Left","Right","B","A"];
var indexkonami=0;
function konami_game(){
    alert("HELLO from js");
}

function konami(key){
    if(key==code[indexkonami]){
        indexkonami++;
        if(indexkonami==8){
            konami_game();
            indexkonami=0;
        }
    }
    else indexkonami=0;
}

document.addEventListener('keydown',(event)=>{
    var name=event.key;
    var namemaj=name.toUpperCase();
    switch(name)
    {
        case "ArrowUp": konami("Up"); break;
        case "ArrowDown": konami("Down"); break;
        case "ArrowLeft": konami("Left"); break;
        case "ArrowRight": konami("Right"); break;
    }
    switch(namemaj){
        case "B": konami("B"); break;
        case "A": konami("A"); break;
    }
})