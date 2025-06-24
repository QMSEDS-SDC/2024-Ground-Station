from flask import Flask, render_template, request, redirect, url_for, make_response, flash, get_flashed_messages, \
    jsonify
import json
import datetime
import fetch_info
import send_info

# Init
app = Flask(__name__)

# app.secret_key
app.secret_key = "dev"  # temporary secret key


# At a Glance Data

init_cookie_set = False
DEFAULT_AT_A_GLANCE_DATA = {
    "on_glance_comm_status": None,
    "on_glance_cpu_usage": None,
    "on_glance_ram_usage": None,
    "on_glance_storage_usage": None,
    "on_glance_error_count": None,
    "on_glance_battery_stats": None,
    "on_glance_internal_temp": None,
    "on_glance_uptime": None,
    "on_glance_cpu_temp": None,
    "on_glance_aocs": None,
    "on_glance_camera_status": None,
}

# Config stuff

DEFAULT_CONFIG = {
    "refresh_time": 15,  # start glance
    "on_glance_comm_status": True,
    "on_glance_cpu_usage": True,
    "on_glance_ram_usage": True,
    "on_glance_storage_usage": True,
    "on_glance_error_count": True,
    "on_glance_battery_stats": True,
    "on_glance_internal_temp": True,
    "on_glance_uptime": True,
    "on_glance_cpu_temp": True,
    "on_glance_aocs": True,
    "on_glance_camera_status": True,
    "credit_dev": True,  # global appearance
    "enable_light_mode": False,
    "enable_save_banner": True,
    "sbc_ip_v4": "127.0.0.0",  # global practical
    "sbc_port": 3141,
    "sbc_message_encryption_key": "",
    "enable_cam_livestream": False,
    "enable_manual_control": False,
    "battery_voltage": (3.0, 4.2),  # phase 1  # temp
    "battery_amps": (0.0, 2.0),  # temp
    "battery_temp": (0.0, 40.0),  # temp
    "internal_temp": (0.0, 50.0),  # temp
    "downlink_freq": (400.0, 450.0),  # temp
    "uplink_freq": (400.0, 450.0),  # temp
    "signal_strength": (-120.0, 0.0),  # temp
    "transmission_rate": (0.0, 10.0),  # temp
    "gyro": (0.0, 360.0),
    "orientation": (0.0, 360.0),
    "reaction_rpm": (0.0, 100.0),  # temp
    "memory_usage": (0.0, 95.0),
    "error_count": (0, 0),
}


def update_config(response, config):
    response.set_cookie('config', json.dumps(config), max_age=60*60*24*314)  # Pi days of cookie :)


def load_config(request):
    global init_cookie_set

    config_json = request.cookies.get('config')
    if config_json is not None:
        return json.loads(config_json)
    else:
        init_cookie_set = False
        return DEFAULT_CONFIG  # enter default config


# 404 Route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Routes
@app.route('/fetch_info')
def get_info():
    # Fetch the required information
    data = {
        'on_glance_uptime': fetch_info.get_uptime(),
        'on_glance_comm_status': fetch_info.get_comm_status(),
        'on_glance_camera_status': fetch_info.get_camera_status(),
        'on_glance_error_count': fetch_info.get_error_count(),
        'on_glance_aocs': fetch_info.get_aocs(),
        'on_glance_battery_stats': fetch_info.get_battery_stats(),
        'on_glance_internal_temp': fetch_info.get_internal_temp(),
        'on_glance_cpu_usage': fetch_info.get_cpu_usage(),
        'on_glance_ram_usage': fetch_info.get_ram_usage(),
        'on_glance_storage_usage': fetch_info.get_storage_usage(),
        'on_glance_cpu_temp': fetch_info.get_cpu_temp()
    }
    return jsonify(data)


@app.route('/')
def index():
    global init_cookie_set
    config = load_config(request)
    if config == DEFAULT_CONFIG and not init_cookie_set:
        response = make_response(redirect(url_for('index')))
        update_config(response, config)
        init_cookie_set = True
        return response

    values = DEFAULT_AT_A_GLANCE_DATA.copy()

    if config["on_glance_comm_status"]:
        values["on_glance_comm_status"] = fetch_info.get_comm_status()
    if config["on_glance_cpu_usage"]:
        values["on_glance_cpu_usage"] = fetch_info.get_cpu_usage()
    if config["on_glance_ram_usage"]:
        values["on_glance_ram_usage"] = fetch_info.get_ram_usage()
    if config["on_glance_storage_usage"]:
        values["on_glance_storage_usage"] = fetch_info.get_storage_usage()
    if config["on_glance_error_count"]:
        values["on_glance_error_count"] = fetch_info.get_error_count()
    if config["on_glance_battery_stats"]:
        values["on_glance_battery_stats"] = fetch_info.get_battery_stats()
    if config["on_glance_internal_temp"]:
        values["on_glance_internal_temp"] = fetch_info.get_internal_temp()
    if config["on_glance_uptime"]:
        seconds = fetch_info.get_uptime()
        values["on_glance_uptime"] = datetime.timedelta(seconds=seconds)
    if config["on_glance_cpu_temp"]:
        values["on_glance_cpu_temp"] = fetch_info.get_cpu_temp()
    if config["on_glance_aocs"]:
        values["on_glance_aocs"] = fetch_info.get_aocs()
    if config["on_glance_camera_status"]:
        values["on_glance_camera_status"] = fetch_info.get_camera_status()

    return render_template('index.html', config=config, values=values)


@app.route('/phase1')
def phase1():
    config_data = load_config(request)
    if config_data == DEFAULT_CONFIG:
        update_config(make_response(redirect(url_for('config'))), config_data)

    aocs_vals = fetch_info.get_aocs()
    battery_vals = fetch_info.get_battery_stats()
    current_time = datetime.datetime.now()
    comms_vals = fetch_info.get_comms_data()
    comms_status = fetch_info.get_comm_status()

    health_check_values = {
        "data_current": current_time.strftime("%d-%m-%Y"),
        "time_current": current_time.strftime("%H:%M"),
        "battery_voltage": battery_vals["voltage"],
        "battery_amps": battery_vals["current"],
        "battery_temp": battery_vals["temp"],
        "internal_temp": fetch_info.get_internal_temp(),
        "downlink_freq": comms_vals["downlink"],
        "uplink_freq": comms_vals["uplink"],
        "signal_strength": comms_vals["signal_strength"],
        "transmission_rate": comms_vals["data_rate"],
        "gyro": (aocs_vals["x_ang_rate"], aocs_vals["y_ang_rate"], aocs_vals["z_ang_rate"]),
        "orientation": (aocs_vals["x_pos"], aocs_vals["y_pos"], aocs_vals["z_pos"]),
        "mock_sun_status": aocs_vals["mock_sun_sensor"],
        "reaction_rpm": aocs_vals["rpm"],
        "camera_status": fetch_info.get_camera_status(),
        "memory_usage": fetch_info.get_ram_usage(),
        "last_comm_date": comms_status["time"],
        "uptime": round(fetch_info.get_uptime()/60, 2),
        "error_count": fetch_info.get_error_count()["error"],
    }

    # Battery
    if not (config_data["battery_voltage"][0] <= health_check_values["battery_voltage"] <= config_data["battery_voltage"][1]):
        health_check_values["battery_status"] = "NOT OK"
    elif not (config_data["battery_amps"][0] <= health_check_values["battery_amps"] <= config_data["battery_amps"][1]):
        health_check_values["battery_status"] = "NOT OK"
    elif not (config_data["battery_temp"][0] <= health_check_values["battery_temp"] <= config_data["battery_temp"][1]):
        health_check_values["battery_status"] = "NOT OK"
    else:
        health_check_values["battery_status"] = "OK"

    # Temperature
    if config_data["internal_temp"][0] <= health_check_values["internal_temp"] <= config_data["internal_temp"][1]:
        health_check_values["temperature_status"] = "OK"
    else:
        health_check_values["temperature_status"] = "NOT OK"

    # Communication
    if not (config_data["downlink_freq"][0] <= health_check_values["downlink_freq"] <= config_data["downlink_freq"][1]):
        health_check_values["comm_status"] = "NOT OK"
    elif not (config_data["uplink_freq"][0] <= health_check_values["uplink_freq"] <= config_data["uplink_freq"][1]):
        health_check_values["comm_status"] = "NOT OK"
    elif not (config_data["signal_strength"][0] <= health_check_values["signal_strength"] <= config_data["signal_strength"][1]):
        health_check_values["comm_status"] = "NOT OK"
    elif not (config_data["transmission_rate"][0] <= health_check_values["transmission_rate"] <= config_data["transmission_rate"][1]):
        health_check_values["comm_status"] = "NOT OK"
    else:
        health_check_values["comm_status"] = "OK"

    # AOCS
    if not (config_data["gyro"][0] <= health_check_values["gyro"][0] <= config_data["gyro"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif not (config_data["gyro"][0] <= health_check_values["gyro"][1] <= config_data["gyro"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif not (config_data["gyro"][0] <= health_check_values["gyro"][2] <= config_data["gyro"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif not (config_data["orientation"][0] <= health_check_values["orientation"][0] <= config_data["orientation"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif not (config_data["orientation"][0] <= health_check_values["orientation"][1] <= config_data["orientation"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif not (config_data["orientation"][0] <= health_check_values["orientation"][2] <= config_data["orientation"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif not (config_data["reaction_rpm"][0] <= health_check_values["reaction_rpm"] <= config_data["reaction_rpm"][1]):
        health_check_values["aocs_status"] = "NOT OK"
    elif health_check_values["mock_sun_status"] != "ACTIVE":
        health_check_values["aocs_status"] = "NOT OK"
    else:
        health_check_values["aocs_status"] = "OK"

    # Payload
    if health_check_values["camera_status"] == "NOT OPERATIONAL":
        health_check_values["payload_status"] = "NOT OK"
    else:
        health_check_values["payload_status"] = "OK"

    # Data and System
    if not (config_data["memory_usage"][0] <= health_check_values["memory_usage"] <= config_data["memory_usage"][1]):
        health_check_values["system_status"] = "NOT OK"
    elif not comms_status["status"]:
        health_check_values["system_status"] = "NOT OK"
    else:
        health_check_values["system_status"] = "OK"

    # Error
    if config_data["error_count"][0] <= health_check_values["error_count"] <= config_data["error_count"][1]:
        health_check_values["error_log"] = "No critical errors detected."
    else:
        health_check_values["error_log"] = "Critical errors detected, check log for details."

    # Overall
    if health_check_values["battery_status"] == "NOT OK" or health_check_values["temperature_status"] == "NOT OK" or health_check_values["comm_status"] == "NOT OK" or health_check_values["aocs_status"] == "NOT OK" or health_check_values["camera_status"] == "NOT OK" or health_check_values["system_status"] == "NOT OK" or health_check_values["error_count"] > 0:
        health_check_values["overall_status"] = "Anomalies detected."
        health_check_values["recommended_action"] = "Solve the issues stated in error log, and rerun the health check."
    else:
        health_check_values["overall_status"] = "No anomalies detected."
        health_check_values["recommended_action"] = "Continue standard operations."

    return render_template('phase1.html', values=health_check_values)


@app.route('/phase2', methods=['GET', 'POST'])
def phase2():
    if request.method == 'POST':
        selected = request.form.getlist('selected')
        images = fetch_info.get_phase2_images()
        targets = {k: images[k][1] for k in selected}
        send_info.send_targets(targets)
        return redirect(url_for('phase2'))
    images = fetch_info.get_phase2_images()
    return render_template('phase2.html', images=images)


@app.route('/phase3')
def phase3():
    return render_template('phase3.html')


@app.route('/log')
def log():
    return render_template('log.html')


@app.route('/config', methods=['GET', 'POST'])
def config():
    config_data = load_config(request)
    if config_data == DEFAULT_CONFIG:
        update_config(make_response(redirect(url_for('config'))), config_data)
    message = None

    if request.method == "POST":
        form_id = request.form.get("form_id")

        if form_id == "at_a_glance_form":
            config_data["refresh_time"] = int(request.form.get("refresh_time"))
            config_data["on_glance_comm_status"] = "on_glance_comm_status" in request.form
            config_data["on_glance_cpu_usage"] = "on_glance_cpu_usage" in request.form
            config_data["on_glance_ram_usage"] = "on_glance_ram_usage" in request.form
            config_data["on_glance_storage_usage"] = "on_glance_storage_usage" in request.form
            config_data["on_glance_error_count"] = "on_glance_error_count" in request.form
            config_data["on_glance_battery_stats"] = "on_glance_battery_stats" in request.form
            config_data["on_glance_internal_temp"] = "on_glance_internal_temp" in request.form
            config_data["on_glance_uptime"] = "on_glance_uptime" in request.form
            config_data["on_glance_cpu_temp"] = "on_glance_cpu_temp" in request.form
            config_data["on_glance_aocs"] = "on_glance_aocs" in request.form
            config_data["on_glance_camera_status"] = "on_glance_camera_status" in request.form

        elif form_id == "phase1_threshold":
            config_data["battery_voltage"] = (
                float(request.form.get("battery_voltage_lower")), float(request.form.get("battery_voltage_upper"))
            )
            config_data["battery_amps"] = (
                float(request.form.get("battery_amps_lower")), float(request.form.get("battery_amps_upper"))
            )
            config_data["battery_temp"] = (
                float(request.form.get("battery_temp_lower")), float(request.form.get("battery_temp_upper"))
            )
            config_data["internal_temp"] = (
                float(request.form.get("internal_temp_lower")), float(request.form.get("internal_temp_upper"))
            )
            config_data["downlink_freq"] = (
                float(request.form.get("downlink_freq_lower")), float(request.form.get("downlink_freq_upper"))
            )
            config_data["uplink_freq"] = (
                float(request.form.get("uplink_freq_lower")), float(request.form.get("uplink_freq_upper"))
            )
            config_data["signal_strength"] = (
                float(request.form.get("signal_strength_lower")), float(request.form.get("signal_strength_upper"))
            )
            config_data["transmission_rate"] = (
                float(request.form.get("transmission_rate_lower")), float(request.form.get("transmission_rate_upper"))
            )
            config_data["gyro"] = (
                float(request.form.get("gyro_lower")), float(request.form.get("gyro_upper"))
            )
            config_data["orientation"] = (
                float(request.form.get("orientation_lower")), float(request.form.get("orientation_upper"))
            )
            config_data["reaction_rpm"] = (
                float(request.form.get("reaction_rpm_lower")), float(request.form.get("reaction_rpm_upper"))
            )
            config_data["memory_usage"] = (
                float(request.form.get("memory_usage_lower")), float(request.form.get("memory_usage_upper"))
            )
            config_data["error_count"] = (
                float(request.form.get("error_count_lower")), float(request.form.get("error_count_upper"))
            )

        elif form_id == "global_appearance_form":
            config_data["credit_dev"] = "enable_credit_dev" in request.form
            config_data["enable_light_mode"] = "enable_light_mode" in request.form
            config_data["enable_save_banner"] = "enable_save_banner" in request.form

        elif form_id == "global_practical_form":
            config_data["sbc_ip_v4"] = request.form.get("sbc_ip_v4")
            config_data["sbc_port"] = int(request.form.get("sbc_port"))
            config_data["sbc_message_encryption_key"] = request.form.get("sbc_message_encryption_key")
            config_data["enable_cam_livestream"] = "enable_cam_livestream" in request.form
            config_data["enable_manual_control"] = "enable_manual_control" in request.form

        if "enable_light_mode" in request.form:
            flash("Dark Mode is the only thing you need! You plebs! >:(    [Everything else is updated successfully!]")
            config_data["enable_light_mode"] = False
        else:
            flash("Config updated successfully!", "error")
        response = make_response(redirect(url_for('config', message=message)))
        update_config(response, config_data)
        return response

    message = get_flashed_messages()
    return render_template("config.html", config=config_data, message=message)
