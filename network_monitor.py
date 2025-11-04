#!/usr/bin/env python3
"""
Network Monitor - A simple tool to monitor network connectivity and performance
"""

import json
import time
import logging
import sys
from datetime import datetime
from typing import Dict, List, Optional
import requests
from ping3 import ping
import psutil


class NetworkMonitor:
    """Main network monitoring class"""

    def __init__(self, config_file: str = "config.json"):
        """Initialize the network monitor with configuration"""
        self.config = self.load_config(config_file)
        self.setup_logging()
        self.failure_count = {}

    def load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: Configuration file '{config_file}' not found")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in configuration file '{config_file}'")
            sys.exit(1)

    def setup_logging(self):
        """Configure logging"""
        log_file = self.config.get('log_file', 'network_monitor.log')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

    def ping_host(self, host: str, timeout: int = 5) -> Optional[float]:
        """Ping a host and return response time in ms"""
        try:
            response_time = ping(host, timeout=timeout)
            if response_time is not None:
                return response_time * 1000  # Convert to milliseconds
            return None
        except Exception as e:
            self.logger.error(f"Ping error for {host}: {e}")
            return None

    def check_http(self, url: str, timeout: int = 5) -> Optional[float]:
        """Check HTTP endpoint and return response time in ms"""
        try:
            start_time = time.time()
            response = requests.get(url, timeout=timeout)
            response_time = (time.time() - start_time) * 1000

            if response.status_code == 200:
                return response_time
            else:
                self.logger.warning(f"HTTP {url} returned status {response.status_code}")
                return None
        except requests.RequestException as e:
            self.logger.error(f"HTTP error for {url}: {e}")
            return None

    def check_target(self, target: Dict) -> bool:
        """Check a single target and log results"""
        name = target.get('name', 'Unknown')
        target_type = target.get('type', 'ping')
        timeout = self.config.get('timeout', 5)

        if target_type == 'ping':
            host = target.get('host')
            response_time = self.ping_host(host, timeout)

            if response_time is not None:
                self.logger.info(f"✓ {name} ({host}): {response_time:.2f}ms")
                return True
            else:
                self.logger.warning(f"✗ {name} ({host}): No response")
                return False

        elif target_type == 'http':
            url = target.get('url')
            response_time = self.check_http(url, timeout)

            if response_time is not None:
                self.logger.info(f"✓ {name} ({url}): {response_time:.2f}ms")
                return True
            else:
                self.logger.warning(f"✗ {name} ({url}): No response")
                return False

        return False

    def get_network_stats(self) -> Dict:
        """Get current network statistics"""
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv,
            'errin': net_io.errin,
            'errout': net_io.errout,
            'dropin': net_io.dropin,
            'dropout': net_io.dropout
        }

    def check_alert_threshold(self, target_name: str, success: bool):
        """Check if alert threshold is reached for a target"""
        if target_name not in self.failure_count:
            self.failure_count[target_name] = 0

        if not success:
            self.failure_count[target_name] += 1
            threshold = self.config.get('alert_threshold', 3)

            if self.failure_count[target_name] >= threshold:
                self.logger.error(f"ALERT: {target_name} has failed {self.failure_count[target_name]} times!")
        else:
            self.failure_count[target_name] = 0

    def run(self):
        """Main monitoring loop"""
        interval = self.config.get('interval', 60)
        targets = self.config.get('targets', [])

        self.logger.info("Network Monitor started")
        self.logger.info(f"Monitoring {len(targets)} targets every {interval} seconds")

        try:
            while True:
                self.logger.info(f"\n{'='*50}")
                self.logger.info(f"Check started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                # Check all targets
                for target in targets:
                    name = target.get('name', 'Unknown')
                    success = self.check_target(target)
                    self.check_alert_threshold(name, success)

                # Log network stats
                stats = self.get_network_stats()
                self.logger.info(f"\nNetwork Stats:")
                self.logger.info(f"  Sent: {stats['bytes_sent'] / (1024**2):.2f} MB")
                self.logger.info(f"  Received: {stats['bytes_recv'] / (1024**2):.2f} MB")
                self.logger.info(f"  Errors: {stats['errin'] + stats['errout']}")

                # Wait for next interval
                time.sleep(interval)

        except KeyboardInterrupt:
            self.logger.info("\nNetwork Monitor stopped by user")
            sys.exit(0)


def main():
    """Entry point"""
    monitor = NetworkMonitor()
    monitor.run()


if __name__ == "__main__":
    main()
