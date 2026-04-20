
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
    deleteBtn.textContent = "❌";
    deleteBtn.onclick = function() {
        removeAnswer(deleteBtn);
    };

    div.appendChild(label);
    div.appendChild(input);
    div.appendChild(deleteBtn);

    container.appendChild(div);
}

function removeAnswer(button) {
    const container = document.getElementById("answers");

    // mindestens 2 Optionen 
    if (container.children.length <= 2) {
        alert("At least 2 options are required!");
        return;
    }

    // löscht genau die Option, zu der der Button gehört
    button.parentElement.remove();
}
