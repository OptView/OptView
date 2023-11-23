"""
This module is the main entry point for the automated control system.

The module contains a main function which is the main entry point for the automated control system.

Example usage:
    python main.py
"""

from dotenv import load_dotenv
import os
from api_integration.thing_speak_state_sender import ThingSpeakStateSender
from automated_system_runner import AutomatedSystemRunner

# Load environment variables
load_dotenv()

# Set up the controller with the appropriate keys and model path
read_channel_id = "2316311"
write_api_key = os.getenv('WRITE_API_KEY')
model_path = "../models/trained_decision_tree_model.pkl"

# Initialize the ThingSpeakStateSender
window_controller = ThingSpeakStateSender(read_channel_id, write_api_key,
                                              model_path)

# Initialize the AutomatedSystemRunner with the controller
system_runner = AutomatedSystemRunner(window_controller)

# Start the automated control system
control_thread = system_runner.run()

# Main loop to listen for the user's input to stop the process
try:
    print("\nStarting the automated control system ---- enter 'stop' to stop the system.",end='\n\n')
    while True:
        command = input().strip().lower()
        if command == 'stop':
            print("Stopping the automated control system...")
            system_runner.stop()
            control_thread.join()  # Wait for the control thread to finish
            break
except KeyboardInterrupt:
    print("\nInterrupt received, stopping the automated control system...")
    system_runner.stop()
    control_thread.join()
finally:
    print("System stopped.")

# Run the system
if __name__ == '__main__':
    system_runner.run()
