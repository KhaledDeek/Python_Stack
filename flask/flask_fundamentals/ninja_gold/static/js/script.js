x = document.querySelectorAll("span")
time  = new Date()
for (let i=0 ; i< x.length ; i++){
    x[i].innerHTML = "  at   "+ time.getHours() + ':' + time.getMinutes() + ':' + time.getSeconds()
}
