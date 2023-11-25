"""
file: test_automated_system_runner.py
date: 25/11/2023
authors: Ziyad Aljaser, Fahad Altamimi
python: 3.9.12
description: This file contains unit tests for the AutomatedSystemRunner class.

The tests include:
    - Testing that the runner correctly initializes
    - Testing that the runner correctly starts a thread
    - Testing that the runner correctly stops a thread
    - Testing that the runner correctly controls the system with an action
    - Testing that the runner correctly controls the system without an action

The tests are run using the unittest module in Python.
To run the tests, run the following command in the terminal:
python -m unittest tests.automated_system.test_automated_system_runner
"""

import unittest
from unittest.mock import MagicMock
from src.automated_system_runner import AutomatedSystemRunner
import time

class TestAutomatedSystemRunner(unittest.TestCase):
    """Test the AutomatedSystemRunner class."""

    def setUp(self):
        """Set up an AutomatedSystemRunner instance for each test."""
        self.mock_controller = MagicMock()
        self.runner = AutomatedSystemRunner(self.mock_controller)

    def test_initialization(self):
        """Test that the runner is initialized correctly."""

        self.assertEqual(self.runner.controller, self.mock_controller)

    def test_initial_running_state(self):
        """Test that the runner is initialized with the correct running state."""

        self.assertTrue(self.runner.running.is_set())

    def test_run_starts_thread(self):
        """Test that the run method starts a thread."""

        self.mock_controller.get_action.return_value = 'open'
        thread = self.runner.run()
        self.assertTrue(thread.is_alive())

        # Allow some time for the thread to execute before stopping it
        time.sleep(1)
        self.runner.stop()
        thread.join()
        self.assertFalse(thread.is_alive())

    def test_stop_method(self):
        """Test that the stop method stops the thread."""

        self.runner.run()
        self.runner.stop()
        self.assertFalse(self.runner.running.is_set())

    def test_automated_control_with_action(self):
        """Test that the runner correctly controls the system with an action."""

        self.mock_controller.get_action.return_value = 'open'
        self.runner.run()
        time.sleep(1)
        self.mock_controller.set_state.assert_called_with('open')
        self.runner.stop()

    def test_automated_control_without_action(self):
        """Test that the runner correctly controls the system without an action."""

        self.mock_controller.get_action.return_value = None
        self.runner.run()
        time.sleep(1)
        self.mock_controller.set_state.assert_not_called()
        self.runner.stop()
