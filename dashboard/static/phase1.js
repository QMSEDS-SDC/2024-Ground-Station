document.getElementById('save-report-button').addEventListener('click', saveReport);

function saveReport() {
    const report = `
--- CubeSat Health Check Report ---
Date: ${document.querySelector('.phase1-section h3:nth-child(1)').innerText.split(': ')[1]}
Time: ${document.querySelector('.phase1-section h3:nth-child(2)').innerText.split(': ')[1]} GMT

--- Power Subsystem ---
Battery Voltage: ${document.querySelectorAll('.phase1-section ul:nth-child(2) li')[0].innerText.split(': ')[1]}
Battery Current: ${document.querySelectorAll('.phase1-section ul:nth-child(2) li')[1].innerText.split(': ')[1]}
Battery Temperature: ${document.querySelectorAll('.phase1-section ul:nth-child(2) li')[2].innerText.split(': ')[1]}
Status: ${document.querySelectorAll('.phase1-section ul:nth-child(2) li')[3].innerText.split(': ')[1]}

--- Thermal Subsystem ---
Internal Temperature: ${document.querySelectorAll('.phase1-section ul:nth-child(3) li')[0].innerText.split(': ')[1]}
Status: ${document.querySelectorAll('.phase1-section ul:nth-child(3) li')[1].innerText.split(': ')[1]}

--- Communication Subsystem ---
Downlink Frequency: ${document.querySelectorAll('.phase1-section ul:nth-child(4) li')[0].innerText.split(': ')[1]}
Uplink Frequency: ${document.querySelectorAll('.phase1-section ul:nth-child(4) li')[1].innerText.split(': ')[1]}
Signal Strength: ${document.querySelectorAll('.phase1-section ul:nth-child(4) li')[2].innerText.split(': ')[1]}
Data Trasmission Rate: ${document.querySelectorAll('.phase1-section ul:nth-child(4) li')[3].innerText.split(': ')[1]}
Status: ${document.querySelectorAll('.phase1-section ul:nth-child(4) li')[4].innerText.split(': ')[1]}

--- ADCS Subsystem ---
Gyroscope: ${document.querySelectorAll('.phase1-section ul:nth-child(5) li')[0].innerText.split(': ')[1]}
Orientation: ${document.querySelectorAll('.phase1-section ul:nth-child(5) li')[1].innerText.split(': ')[1]}
Mock Sun Sensor: ${document.querySelectorAll('.phase1-section ul:nth-child(5) li')[2].innerText.split(': ')[1]}
Reaction Wheel RPM: ${document.querySelectorAll('.phase1-section ul:nth-child(5) li')[3].innerText.split(': ')[1]}
Status: ${document.querySelectorAll('.phase1-section ul:nth-child(5) li')[4].innerText.split(': ')[1]}

--- Payload Subsystem ---
Camera: ${document.querySelectorAll('.phase1-section ul:nth-child(6) li')[0].innerText.split(': ')[1]}
Status: ${document.querySelectorAll('.phase1-section ul:nth-child(6) li')[1].innerText.split(': ')[1]}

--- Command and Data Handling Subsystem ---
Memory Usage: ${document.querySelectorAll('.phase1-section ul:nth-child(7) li')[0].innerText.split(': ')[1]}
Last Command Received: ${document.querySelectorAll('.phase1-section ul:nth-child(7) li')[1].innerText.split(': ')[1]} GMT
Uptime: ${document.querySelectorAll('.phase1-section ul:nth-child(7) li')[2].innerText.split(': ')[1]}
Status: ${document.querySelectorAll('.phase1-section ul:nth-child(7) li')[3].innerText.split(': ')[1]}

--- Error Log ---
${document.querySelectorAll('.phase1-section ul:nth-child(8) li')[0].innerText}

--- Overall Status ---
${document.querySelectorAll('.phase1-section ul:nth-child(9) li')[0].innerText}
Recommended Actions: ${document.querySelectorAll('.phase1-section ul:nth-child(9) li')[1].innerText.split(': ')[1]}

--- End of Report ---
`;

    const blob = new Blob([report], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'CubeSat_Health_Check_Report.txt';
    link.click();
}
