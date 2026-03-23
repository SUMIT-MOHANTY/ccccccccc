import unittest
import subprocess
import time
import requests
import os
import signal
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("test_api.log")
    ]
)
logger = logging.getLogger(__name__)

class TestFlaskCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("Setting up test environment")
        # Start Flask app in a separate process
        cmd = [sys.executable, "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
        cls.flask_process = subprocess.Popen(
            cmd,
            env={**os.environ, "FLASK_APP": "flask-calculator/app.py", "PORT": "5001"},
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Check if the process started correctly
        logger.info(f"Flask process PID: {cls.flask_process.pid}")

        # Allow Flask time to initialize
        max_attempts = 30
        attempts = 0
        base_url = "http://localhost:5001"

        while attempts < max_attempts:
            try:
                response = requests.get(f"{base_url}/health")
                if response.status_code == 200:
                    logger.info("Flask application is ready for testing")
                    break
            except requests.exceptions.ConnectionError:
                logger.info(f"Waiting for Flask to start (attempt {attempts+1}/{max_attempts})")
                time.sleep(1)
            attempts += 1

        if attempts >= max_attempts:
            logger.error("Failed to start Flask application")
            cls.tearDownClass()
            raise Exception("Flask application failed to start")

    @classmethod
    def tearDownClass(cls):
        logger.info("Tearing down test environment")
        if hasattr(cls, 'flask_process'):
            logger.info(f"Terminating Flask process (PID: {cls.flask_process.pid})")
            try:
                # Send SIGTERM to the process group
                os.kill(cls.flask_process.pid, signal.SIGTERM)
                # Give it some time to shutdown gracefully
                cls.flask_process.wait(timeout=5)
                logger.info("Flask process terminated successfully")
            except Exception as e:
                logger.error(f"Error terminating Flask process: {e}")
                try:
                    # Force kill if necessary
                    os.kill(cls.flask_process.pid, signal.SIGKILL)
                    logger.info("Flask process forcefully terminated")
                except:
                    logger.error("Failed to kill Flask process")

    def test_add(self):
        response = requests.post(
            "http://localhost:5001/add",
            json={"a": 2, "b": 3}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["result"], 5)

    def test_add_invalid_input(self):
        response = requests.post(
            "http://localhost:5001/add",
            json={"a": "not a number", "b": 3}
        )
        self.assertEqual(response.status_code, 400)

    def test_subtract(self):
        response = requests.post(
            "http://localhost:5001/subtract",
            json={"a": 5, "b": 3}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["result"], 2)

if __name__ == "__main__":
    unittest.main()
