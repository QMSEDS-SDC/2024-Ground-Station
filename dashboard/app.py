from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response, flash, \
    get_flashed_messages
import json
import fetch_info

# Init
app = Flask(__name__)

# app.secret_key
app.secret_key = "dev"  # temporary secret key


# Config stuff

DEFAULT_CONFIG = {
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
    config_json = request.cookies.get('config')
    if config_json is not None:
        return json.loads(config_json)
    else:
        return DEFAULT_CONFIG  # enter default config


# Routes
@app.route('/')
def index():
    return render_template('index.html', config=load_config(request))


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
    message = None

    if request.method == "POST":
        form_id = request.form.get("form_id")

        if form_id == "at_a_glance_form":
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

        flash("Config updated successfully!")
        response = make_response(redirect(url_for('config', message=message)))
        update_config(response, config_data)
        return response

    message = get_flashed_messages()
    return render_template("config.html", config=config_data, message=message)
