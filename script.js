const terminalOutput = document.getElementById('terminalOutput');
const cursor = document.getElementById('cursor');
const dataVisualization = document.getElementById('dataVisualization');
let outputIndex = 0;

const commands = [
    "Fetching OSINT data...",
    "Analyzing packets...",
    "Scanning for vulnerabilities...",
    "Data retrieval complete!",
    "Generating report..."
];

// Simulate terminal output with a blinking cursor
function simulateTerminal() {
    if (outputIndex < commands.length) {
        terminalOutput.innerHTML += `<div>${commands[outputIndex]}</div>`;
        outputIndex++;
        setTimeout(simulateTerminal, 2000);
    } else {
        cursor.style.visibility = cursor.style.visibility === 'visible' ? 'hidden' : 'visible';
        setInterval(() => cursor.style.visibility = cursor.style.visibility === 'visible' ? 'hidden' : 'visible', 500);
    }
}

// Update data visualization dynamically
function updateVisualization() {
    const randomData = Math.floor(Math.random() * 100);
    dataVisualization.style.height = `${randomData}%`;
    dataVisualization.innerHTML = `${randomData}% detected threats`;
    setTimeout(updateVisualization, 3000);
}

// Start terminal simulation and visualization
document.addEventListener('DOMContentLoaded', () => {
    simulateTerminal();
    updateVisualization();
});
```

Make sure to have HTML elements with IDs `terminalOutput`, `cursor`, and `dataVisualization` for the JavaScript to interact with.