let count = 2;

function addAnswer() {
    const container = document.querySelector(".answers");

    const div = document.createElement("div");
    div.className = "option";

    const label = document.createElement("p");

    const row = document.createElement("div");
    row.className = "option-row";

    const input = document.createElement("input");
    input.type = "text";
    input.name = "answer";
    input.placeholder = "Answer";

    const deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.textContent = "❌";

    deleteBtn.onclick = function () {
        removeAnswer(div);
    };

    row.appendChild(input);
    row.appendChild(deleteBtn);

    div.appendChild(label);
    div.appendChild(row);

    container.appendChild(div);

    renumberAnswers();
}

function removeAnswer(button) {
    const container = document.querySelector(".answers");

    if (container.children.length <= 2) {
        alert("At least 2 options are required!");
        return;
    }

    const optionDiv = button.closest(".option"); // 🔥 wichtig
    optionDiv.remove();

    renumberAnswers();
}

function renumberAnswers() {
    const options = document.querySelectorAll(".option");

    options.forEach((option, index) => {
        const number = index + 1;

        const label = option.querySelector("p");
        const input = option.querySelector("input");

        if (label) {
            label.textContent = "Option " + number + ":";
        }

        if (input) {
            input.placeholder = "Answer " + number;
        }
    });

    count = options.length;
}


