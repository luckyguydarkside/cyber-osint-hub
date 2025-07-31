document.addEventListener('DOMContentLoaded', () => {
    const dashboard = document.querySelector('#dashboard-container');
    const terminalOutput = document.createElement('pre');
    terminalOutput.style.fontFamily = 'monospace';
    
    const commands = [
        'Fetching OSINT data...',
        'Connecting to data sources...',
        'Data retrieval complete!',
        'Displaying results...'
    ];

    commands.forEach((cmd, index) => {
        setTimeout(() => {
            terminalOutput.textContent += `$ ${cmd}\n`;
            dashboard.appendChild(terminalOutput);
        }, index * 1500);
    });
});