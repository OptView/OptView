"""
This module runs the window automation system.

The module contains an AutomatedSystemRunner class
 which can be used to run the window automation system.
"""

import threading
import time


class AutomatedSystemRunner:
    """A class used to run the window automation system."""

    def __init__(self, controller):
        """Initialize the AutomatedSystemRunner with a controller.

        Args:
            controller (ThingSpeakStateSender): The controller to use to control the window state.
        """
        self.controller = controller
        self.running = threading.Event()
        self.running.set()  # Start with the event set to True

    def run(self):
        """Run the window automation system in a separate thread."""

        def automated_control():
            while self.running.is_set():
                action = self.controller.get_action()

                if action is not None:
                    print(f"Action: {action}")
                    self.controller.set_state(action)
                else:
                    print("Failed to retrieve sensor data.")

                print("Sleeping...", end='\n\n')
                time.sleep(15)

        control_thread = threading.Thread(target=automated_control)
        control_thread.start()

        return control_thread

    def stop(self):
        """Stop the window automation system."""
        self.running.clear()  # Clear the event to stop the loop
