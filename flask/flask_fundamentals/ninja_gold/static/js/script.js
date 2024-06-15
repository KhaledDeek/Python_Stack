x = document.querySelectorAll(".time")
time  = new Date()
for (let i=0 ; i< x.length ; i++){
    x[i].innerHTML = time.getHours() + ':' + time.getMinutes() + ':' + time.getSeconds()
}
