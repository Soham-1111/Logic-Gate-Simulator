function calculateOutput() {
    const input1 = document.getElementById("input1").value;
    const selectedGate = document.getElementById("gate").value;
    let output;

    // Check if the selected gate is NOT
    if (selectedGate === "NOT") {
        if (input1 !== "0" && input1 !== "1") {
            alert("Invalid input for NOT gate. Please enter 0 or 1 for Input 1.");
            return;
        }
        output = input1 === "0" ? 1 : 0;
    } else {
        const input2 = document.getElementById("input2").value;
        if ((input1 !== "0" && input1 !== "1") || (input2 !== "0" && input2 !== "1")) {
            alert("Invalid input. Please use 0 or 1 for both inputs.");
            return;
        }

        const in1 = parseInt(input1);
        const in2 = parseInt(input2);

        switch (selectedGate) {
            case "AND":
                output = in1 & in2;
                break;
            case "OR":
                output = in1 | in2;
                break;
            case "NAND":
                output = !(in1 & in2) ? 1 : 0;
                break;
            case "NOR":
                output = !(in1 | in2) ? 1 : 0;
                break;
            case "XOR":
                output = in1 ^ in2;
                break;
            case "XNOR":
                output = in1 === in2 ? 1 : 0;
                break;
            default:
                output = "Invalid";
        }
    }

    document.getElementById("output").innerText = `Output: ${output}`;
}

function toggleInput2() {
    const selectedGate = document.getElementById("gate").value;
    const input2 = document.getElementById("input2");

    // Disable input2 and set it as readonly if the selected gate is NOT
    if (selectedGate === "NOT") {
        input2.disabled = true;
        input2.readOnly = true; // Make sure it's also readonly
        input2.value = ""; // Clear the value of input2
    } else {
        input2.disabled = false;
        input2.readOnly = false; // Remove readonly
    }
}

// Initialize the dropdown change on page load
window.onload = () => {
    document.getElementById("gate").addEventListener("change", toggleInput2);
    toggleInput2(); // Call it initially to set the correct state on page load
};
