// Simple OSINT Dashboard Enhancer
const terminalOutput = document.getElementById('terminalOutput');
const cursor = document.createElement('span');
cursor.className = 'cursor';
cursor.textContent = '|';
terminalOutput.appendChild(cursor);

const commands = [
    "Scanning for open ports...",
    "Collecting metadata from websites...",
    "Fetching DNS records...",
    "Analyzing network traffic...",
    "Gathering geographical data..."
];

let commandIndex = 0;

function typeCommand() {
    if (commandIndex < commands.length) {
        let command = commands[commandIndex];
        terminalOutput.innerHTML += `<div>${command}</div>`;
        commandIndex++;
        setTimeout(typeCommand, 2000);
    } else {
        cursor.style.display = 'none'; // Hide cursor after commands
    }
}

function toggleCursor() {
    cursor.style.visibility = (cursor.style.visibility === 'hidden') ? 'visible' : 'hidden';
}

setInterval(toggleCursor, 500);
typeCommand();

// Dynamic data visualization
const updateDataButton = document.getElementById('updateData');
const dataDisplay = document.getElementById('dataDisplay');

updateDataButton.addEventListener('click', () => {
    const newData = Math.floor(Math.random() * 100);
    dataDisplay.textContent = `Current Threat Level: ${newData}`;
    dataDisplay.style.color = newData > 70 ? 'red' : 'green';
});
```

Make sure you include an HTML structure that has elements with the IDs `terminalOutput`, `updateData`, and `dataDisplay` for the above JavaScript to work effectively.