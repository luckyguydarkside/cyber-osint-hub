// OSINT Dashboard Interactive Script
const terminalOutput = document.getElementById('terminal-output');
const cursor = document.getElementById('cursor');
const dataVisual = document.getElementById('data-visual');

let outputLines = [
    "Fetching OSINT data...",
    "Analyzing IP address...",
    "Gathering social media footprints...",
    "Scanning public records...",
    "Data retrieval complete!",
    "Visualizing results..."
];

let index = 0;

function typeWriterEffect(line, callback) {
    let i = 0;
    const interval = setInterval(() => {
        if (i < line.length) {
            terminalOutput.innerHTML += line.charAt(i);
            i++;
        } else {
            clearInterval(interval);
            setTimeout(callback, 1000); // Wait before next line
        }
    }, 100);
}

function simulateTerminal() {
    if (index < outputLines.length) {
        typeWriterEffect(outputLines[index], () => {
            index++;
            simulateTerminal();
        });
    } else {
        displayVisualization();
    }
}

function displayVisualization() {
    terminalOutput.innerHTML += "<br>✔ All tasks completed!";
    dataVisual.style.display = 'block';
    // Simulate dynamic data visualization update
    setInterval(() => {
        dataVisual.innerHTML = `Updated Data: ${Math.floor(Math.random() * 100)}`;
    }, 2000);
}

function blinkCursor() {
    setInterval(() => {
        cursor.style.opacity = cursor.style.opacity === '0' ? '1' : '0';
    }, 500);
}

document.addEventListener('DOMContentLoaded', () => {
    simulateTerminal();
    blinkCursor();
});
```