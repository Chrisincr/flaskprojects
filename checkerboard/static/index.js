function setColors(pcolor, scolor){
    let doc = document.getElementsByTagName('html')[0];
    doc.style.setProperty("--pcolor", pcolor)
    doc.style.setProperty("--scolor", scolor)
}