async function fetchInfo() {
    try {
        const response = await fetch('/fetch_info');
        const data = await response.json();

        // Update the values on the page with the fetched data
        document.querySelectorAll('.status-item').forEach(item => {
            const h3 = item.querySelector('h3').textContent;
            if (h3.includes("Uptime")) {
                item.querySelector('p').textContent = data.on_glance_uptime + ' (hr:min:sec)';
            } else if (h3.includes("Communication System Status")) {
                item.querySelector('p').textContent = data.on_glance_comm_status ? 'Operational' : 'Not Operational';
            } else if (h3.includes("Camera Status")) {
                item.querySelector('p').textContent = data.on_glance_camera_status ? 'Operational' : 'Not Operational';
            } else if (h3.includes("Error Count")) {
                item.querySelector('p').textContent = 'Errors: ' + data.on_glance_error_count.error;
                item.querySelector('p + p').textContent = 'Warnings: ' + data.on_glance_error_count.warning;
            } else if (h3.includes("AOCS Stats")) {
                item.querySelector('p').textContent = 'Position Angle: (' + data.on_glance_aocs.x + ', ' + data.on_glance_aocs.y + ', ' + data.on_glance_aocs.z + ')';
                item.querySelector('p + p').textContent = 'RPM: ' + data.on_glance_aocs.rpm + ' rpm';
                item.querySelector('p + p + p').textContent = data.on_glance_aocs ? 'Operational' : 'Not Operational';
            } else if (h3.includes("Battery Stats")) {
                item.querySelector('p').textContent = 'Charge: ' + data.on_glance_battery_stats.percentage + '%';
                item.querySelector('p + p').textContent = 'Voltage: ' + data.on_glance_battery_stats.voltage + 'V';
                item.querySelector('p + p + p').textContent = 'Current: ' + data.on_glance_battery_stats.current + 'A';
            } else if (h3.includes("Internal Temperature")) {
                item.querySelector('p').textContent = data.on_glance_internal_temp + '°C';
            } else if (h3.includes("CPU Usage")) {
                item.querySelector('p').textContent = data.on_glance_cpu_usage + '%';
            } else if (h3.includes("RAM Usage")) {
                item.querySelector('p').textContent = data.on_glance_ram_usage + '%';
            } else if (h3.includes("Storage Usage")) {
                item.querySelector('p').textContent = data.on_glance_storage_usage + '%';
            } else if (h3.includes("CPU Temperature")) {
                item.querySelector('p').textContent = data.on_glance_cpu_temp + '%';
            }
        });
    } catch (error) {
        console.error('Error fetching info:', error);
    }
}

function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    for (let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");
        if (name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1].replace(/\+/g, ' '));
        }
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function() {
    let rawConfig = getCookie('config');
    rawConfig = rawConfig.slice(1, -1);
    rawConfig = rawConfig.replace(/\\"/g, '"').replace(/\\054/g, ',');
    let config = JSON.parse(rawConfig);

    console.log('Config:', config);
    const interval = config.refresh_time * 1000; // Convert to milliseconds
    setInterval(fetchInfo, interval);
    fetchInfo();
});
