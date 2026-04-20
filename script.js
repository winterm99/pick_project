
let count = 2;

function addAnswer() {
    count++;

    const container = document.getElementById("answers");

    const div = document.createElement("div");
    div.className = "option";

    const label = document.createElement("p");
    label.textContent = "Option " + count + ":";

    const input = document.createElement("input");
    input.type = "text";
    input.name = "answer";
    input.placeholder = "Answer " + count;
    
    const deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.textContent = "x";
    deleteBtn.onclick = function() {
        removeAnswer(deleteBtn);
    };

    div.appendChild(label);
    div.appendChild(input);
    div.appendChild(deleteBtn);

    container.appendChild(div);
}
