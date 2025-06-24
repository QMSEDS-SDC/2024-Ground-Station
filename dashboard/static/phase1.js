document.addEventListener('DOMContentLoaded', function() {
    const saveBtn = document.getElementById('save-report-button');
    if (saveBtn) {
        saveBtn.disabled = false;
        saveBtn.style.cursor = 'pointer';
        saveBtn.innerText = 'Save Report';
        saveBtn.addEventListener('click', function() {
            const sections = document.querySelectorAll('.phase1-section');
            let report = '--- CubeSat Health Check Report ---\n';
            sections.forEach(section => {
                const header = section.querySelector('h2,h3');
                if (header) report += `\n${header.innerText}\n`;
                const list = section.querySelector('ul');
                if (list) {
                    list.querySelectorAll('li').forEach(li => {
                        report += `${li.innerText}\n`;
                    });
                }
            });
            report += '\n--- End of Report ---\n';
            const blob = new Blob([report], { type: 'text/plain' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'CubeSat_Health_Check_Report.txt';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(link.href);
        });
    }
});