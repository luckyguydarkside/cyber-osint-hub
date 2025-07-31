document.addEventListener('DOMContentLoaded', () => {
    const terminalOutput = document.getElementById('terminal-output');
    const cursor = document.createElement('span');
    cursor.innerHTML = '|';
    cursor.className = 'blinking-cursor';
    terminalOutput.appendChild(cursor);

    const commands = [
        'Initializing OSINT tool...',
        'Scanning networks...',
        'Gathering data...',
        'Analysis complete: 5 vulnerabilities found.',
        'Generating report...'
    ];
    
    let index = 0;
    
    function typeCommand() {
        if (index < commands.length) {
            terminalOutput.innerHTML += `<div>${commands[index]}</div>`;
            index++;
            setTimeout(typeCommand, 2000);
        } else {
            cursor.style.display = 'none';
        }
    }

    typeCommand();

    const dynamicData = document.getElementById('dynamic-data');
    const updateButton = document.getElementById('update-button');
    
    updateButton.addEventListener('click', () => {
        const randomData = Math.floor(Math.random() * 100);
        dynamicData.innerHTML = `Latest Threat Level: ${randomData}`;
    });

    setInterval(() => {
        const date = new Date();
        document.getElementById('timestamp').innerHTML = `Last updated: ${date.toLocaleTimeString()}`;
    }, 5000);
});
```

To use this script, ensure you have a corresponding HTML structure with elements having IDs `terminal-output`, `dynamic-data`, `update-button`, and `timestamp`.