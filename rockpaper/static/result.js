function showImg(img){
    let doc =document.getElementsByClassName(img)
    
    for (let i = 0; i<doc.length; i++){
        doc[i].style.display = "inline-block"
    }
}