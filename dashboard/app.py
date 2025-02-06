from flask import Flask, render_template, request, redirect, url_for, make_response, flash, get_flashed_messages, \
    jsonify, session
import json
import datetime
import fetch_info

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
    "refresh_time": 5,
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
    "credit_dev": True,
    "enable_light_mode": False,
    "enable_save_banner": True,
    "sbc_ip_v4": "127.0.0.0",
    "sbc_port": 3141,
    "sbc_message_encryption_key": "",
    "enable_cam_livestream": False,
    "enable_manual_control": False,
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
    return render_template('phase1.html')


@app.route('/phase2')
def phase2():
    return render_template('phase2.html')


@app.route('/phase3')
def phase3():
    return render_template('phase3.html')


@app.route('/log')
def log():
    return render_template('log.html')


@app.route('/config', methods=['GET', 'POST'])
def config():
    config_data = load_config(request)
    if config == DEFAULT_CONFIG:
        update_config(make_response(redirect(url_for('config'))), config)
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
