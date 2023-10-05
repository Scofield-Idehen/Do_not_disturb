
# Website Blocker App

## Overview

The Website Blocker App is a Python script designed to help users stay focused during work hours by blocking access to specific websites. It achieves this by modifying the system's hosts file to redirect designated web addresses to a local IP address (127.0.0.1), effectively preventing access to those sites. The script restores normal access during non-working hours.

## Features

- Blocks access to specified websites during working hours.
- Allows unrestricted access during non-working hours.
- Easily customizable list of banned websites.
- Utilizes the system's hosts file for redirection.

## Requirements

To use this script, you'll need the following:

- Python 3.x
- Administrative privileges to modify the hosts file (typically located at `/etc/hosts` on Unix-like systems).

## Usage

Follow these steps to use the Website Blocker App:

1. Open the script in a text editor or integrated development environment (IDE) of your choice.

2. Customize the following variables to match your preferences:

   - `host_path`: The path to your system's hosts file. By default, it's set to `/etc/hosts`, but you may need to adjust this for Windows or other operating systems.

   - `redirect`: The IP address to which blocked websites will be redirected. The default is `127.0.0.1`, which points to your own machine.

   - `banned_list`: A list of websites you want to block. Add or remove websites from this list to control which sites are blocked during working hours.

3. Save the script after making your changes.

4. Run the script with administrative privileges. This is crucial for modifying the hosts file. On Unix-like systems (e.g., Linux or macOS), use `sudo`:

   ```shell
   sudo python your_script_name.py
On Windows, run your script as an administrator.

The script will run continuously, checking the time. During your specified working hours, the listed websites will be blocked. Access will be restored during non-working hours.

To stop the script, press Ctrl+C in the terminal where it's running.

Important Notes
Exercise caution when editing system files like the hosts file, as incorrect changes can impact your network configuration.

This script is a basic example and may not cover all use cases or operating systems. Customize it to meet your specific requirements.

Use this script responsibly and in accordance with your workplace's policies and local laws.

Make sure to back up your hosts file before running the script to avoid unintended consequences.

The script will run indefinitely until manually terminated. Ensure you have a way to stop it when necessary.

License
This script is provided under the MIT License. You are free to modify and distribute it as needed. Please refer to the LICENSE file for detailed licensing information.