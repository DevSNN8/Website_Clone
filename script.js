const redBtn = document.getElementById("redBtn");
const greeBtn = document.getElementById("greeBtn");
const yelBtn = document.getElementById("yelBtn");
const defBtn = document.getElementById("defBtn");
const mbox = document.getElementById("mbox");


redBtn.addEventListener("click", () => {
    mbox.style.backgroundColor ="red";
})


greeBtn.addEventListener("click", () => {
    mbox.style.backgroundColor ="green";
})

yelBtn.addEventListener("click", () => {
    mbox.style.backgroundColor ="yellow";
})

defBtn.addEventListener("click", () => {
    mbox.style.backgroundColor ="black";
})