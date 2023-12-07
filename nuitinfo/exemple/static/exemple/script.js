
// Konami code

const code=["Up","Up","Down","Down","Left","Right","B","A"];
var indexkonami=0;
function konami_game(){
    alert("HELLO from js");
}

function konami(key){
    if(key==code[indexkonami]){
        indexkonami++;
        if(indexkonami==9){
            konami_game();
        }
    }
    else indexkonami=0;
}


document.eventEventListener('keypress',(event)=>{
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
        case "A": konami("A"); break;
        case "B": konami("B"); break;
    }
})