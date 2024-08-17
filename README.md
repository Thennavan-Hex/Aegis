# Aegis

**Aegis** is a network operations tool designed to facilitate the management and monitoring of ESP32 devices through a command-line interface (CLI). The tool provides functionalities for uploading code to the ESP32, monitoring serial output, and detecting connected devices.

## Features

- **Upload Code:** Upload Arduino sketches to ESP32 devices.
- **Monitor Serial Output:** Continuously monitor the serial output from ESP32 devices.
- **Detect Connected Devices:** Automatically detect and list connected ESP32 devices on serial ports.

## Pre-requisites

Before using Aegis, ensure you have the following:

- **Python 3.12** or higher installed on your system.
- **Arduino CLI** installed and configured. [Install Arduino CLI](https://arduino.github.io/arduino-cli/latest/installation/).
  
## Installation

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:Thennavan-Hex/Aegis.git
   cd Aegis
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Python Packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Monitor Serial Output:**

   To monitor the serial output from the ESP32:

   ```bash
   python main.py scan
   ```

2. **Upload Code to ESP32:**

   To upload code to the ESP32 device:

   ```bash
   python main.py scan -u
   ```

   Ensure that the Arduino sketch (`scan.ino`) is located in the `Code` directory.

## Contributing

Contributions to the Aegis project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your modifications and test them.
4. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact the project maintainer:

- **Thennavan**: [GitHub Profile](https://github.com/Thennavan-Hex)

### Notes:
- Make sure to adjust the sections according to your project specifics, such as contributing guidelines and license details.
- The paths and commands are based on standard practices; adjust them if your setup differs.
