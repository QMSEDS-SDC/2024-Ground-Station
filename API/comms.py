import socket
import json
import os
import threading
import time


class Client_Comms:
    """
    To send commands and get stuff from CubeSat
    """
    
    def __init__(self, port_code="MAIN_PORT"):
        # contains info that is common with cubesat
        env_path = os.path.join(os.path.dirname(__file__), "env_values.json")
        with open(env_path, "r") as f:
            self.env = json.load(f)
        
        self.receive_host = self.env["CUBESAT_HOST"]
        self.receive_port = self.env[port_code]
        
        self.client_socket = None
        self.connected = False
        self.running = False
        self.receive_thread = None        

        # response storage
        self.last_response = None
        self.response_received = threading.Event()
    
    def connect(self):
        """Connect to the cubesat"""
        host = self.receive_host
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.settimeout(10)  # set 10 seconds as the timeout for conn
            self.client_socket.connect((host, self.receive_port))            
            self.connected = True
            self.running = True
            
            # use threading
            self.receive_thread = threading.Thread(target=self._receive_loop)
            self.receive_thread.daemon = True
            self.receive_thread.start()
            
            return True
            
        except (socket.gaierror, ConnectionRefusedError, OSError, socket.timeout):  # these are potential exceptions
            if self.client_socket:  # close em up
                self.client_socket.close()
                self.client_socket = None
        
        return False
    
    def _receive_loop(self):
        """Always allow to receive messages"""
        while self.running and self.connected:
            try:
                # Receive data from server
                data = self.client_socket.recv(1024).decode("utf-8")

                if not data:
                    self.connected = False
                    break
                
                # Process single JSON message (remove buffer logic)
                if data.strip():
                    try:
                        json_message = json.loads(data.strip())
                        self.handle_received_message(json_message)
                    except json.JSONDecodeError:
                        pass
                    
            except socket.timeout:
                continue
            except ConnectionResetError:
                self.connected = False
                break
            except Exception:
                self.connected = False
                break
    
    def handle_received_message(self, json_message):
        """Process received JSON messages from server"""
        message_type = json_message.get("type", "NA")
    
        if message_type == "status":
            response = json_message.get("message", [])
            print(f"Status received: {response}")
            # TODO: Call GUI update function - gui.update_sensor_status(response)
            return response
    
        elif message_type == "response":
            result = json_message.get("message", 0)
            print(f"Operation response: {result}")
            # TODO: Call GUI update function - gui.update_operation_result(result)
            return result
    
        elif message_type == "p2_info":
            payload_data = json_message.get("message", {})
            print(f"Payload 2 info: {payload_data}")
            # TODO: Call GUI update function - gui.update_payload2_info(payload_data)
            return payload_data
    
        elif message_type == "p2_cmd":
            command_results = json_message.get("message", {})
            print(f"Payload 2 command results: {command_results}")
            # TODO: Call GUI update function - gui.update_payload2_commands(command_results)
            return command_results
    
        elif message_type == "p3_info":
            payload3_data = json_message.get("message", {})
            print(f"Payload 3 info: {payload3_data}")
            # TODO: Call GUI update function - gui.update_payload3_info(payload3_data)
            return payload3_data
    
        elif message_type == "img":
            image_data = json_message.get("message", [])
            print(f"Image data received (length: {len(image_data)})")
            # TODO: Call GUI update function - gui.display_image(image_data)
            return image_data
    
        elif message_type == "Error":
            error_code = json_message.get("message", -1)
            print(f"Server error code: {error_code}")
            # TODO: Call GUI update function - gui.show_error(error_code)
            return error_code
            
        else:
            print(f"Unknown message type: {message_type}")
            # TODO: Call GUI update function - gui.log_unknown_message(json_message)
            return None
    
    def send_json_message(self, message_data):
        """Send JSON message to server"""
        if not self.connected or not self.client_socket:
            return False

        try:
            # Remove newline delimiter - send pure JSON
            json_string = json.dumps(message_data)
            self.client_socket.sendall(json_string.encode("utf-8"))
            return True
        except Exception:
            self.connected = False
            return False
    
    def disconnect(self):
        """Gracefully disconnect from server"""
        if self.connected:
            self.send_json_message({"type": "disconnect"})
            time.sleep(0.5)  # Give server time to process disconnect
        
        self.running = False
        self.connected = False
        
        if self.client_socket:
            try:
                self.client_socket.close()
            except Exception:
                pass
            self.client_socket = None
        
        if self.receive_thread and self.receive_thread.is_alive():
            self.receive_thread.join(timeout=2)
            
    def is_connected(self):
        """Check if client is connected"""
        return self.connected
    
    def wait_for_messages(self, duration=None):
        """Wait for incoming messages for a specified duration"""
        if duration:
            time.sleep(duration)
        else:
            try:
                while self.connected:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("\nStopping message wait...")

    # Send functions for each message type
    def request_status(self, sensors_list):
        """Request status of specific sensors"""
        message = {
            "type": "status",
            "message": sensors_list
        }
        return self.send_json_message(message)

    def initialise_phase(self, phase_number):
        """Initialise a specific phase"""
        message = {
            "type": "init",
            "message": phase_number
        }
        return self.send_json_message(message)

    def get_payload2_info(self):
        """Get payload 2 information"""
        message = {
            "type": "p2_info",
            "message": "get"
        }
        return self.send_json_message(message)

    def send_payload2_command(self, targets_list):
        """Send command to payload 2 targets"""
        message = {
            "type": "p2_cmd",
            "message": targets_list
        }
        return self.send_json_message(message)

    def get_payload3_info(self):
        """Get payload 3 information"""
        message = {
            "type": "p3_info",
            "message": "get"
        }
        return self.send_json_message(message)

    def request_image(self):
        """Request image data"""
        message = {
            "type": "img",
            "message": "get"
        }
        return self.send_json_message(message)

    def shutdown_cubesat(self, seconds):
        """Shutdown cubesat after specified seconds"""
        message = {
            "type": "shutdown",
            "message": seconds
        }
        return self.send_json_message(message)

    def send_optional_command(self, feature):
        """Send optional command (live or manual)"""
        message = {
            "type": "optional",
            "message": feature
        }
        return self.send_json_message(message)
