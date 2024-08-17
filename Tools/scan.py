import argparse
import os
import subprocess
import sys
import serial
from rich.console import Console
from check_port import check_connections

console = Console()

def compile_sketch(sketch_path, fqbn):
    """Compile the Arduino sketch."""
    compile_command = [
        "arduino-cli", "compile",
        "--fqbn", fqbn,
        sketch_path
    ]
    try:
        result = subprocess.run(compile_command, check=True, text=True, capture_output=True)
        console.print(result.stdout)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error during compilation:\n{e.stderr}[/red]")
        sys.exit(1)

def upload_code(port, sketch_path, fqbn):
    """Upload the compiled Arduino sketch."""
    compile_sketch(sketch_path, fqbn)
    
    upload_command = [
        "arduino-cli", "upload",
        "-p", port,
        "--fqbn", fqbn,
        sketch_path
    ]
    try:
        result = subprocess.run(upload_command, check=True, text=True, capture_output=True)
        console.print(result.stdout)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error during upload:\n{e.stderr}[/red]")
        sys.exit(1)

def monitor_serial(port):
    try:
        with serial.Serial(port, baudrate=115200, timeout=1) as ser:
            console.print(f"[bold green]Monitoring serial port: {port}[/bold green]")
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    # Ignore lines starting with 'rst:'
                    if line and not line.startswith('rst:'):
                        console.print(f"[cyan]{line}[/cyan]")
    except serial.SerialException as e:
        console.print(f"[red]Error: {e}[/red]")
    except KeyboardInterrupt:
        console.print("[bold yellow]Monitoring stopped by user.[/bold yellow]")

def main(upload=False):
    esp32_ports = check_connections()
    if esp32_ports:
        port = esp32_ports[0]
        sketch_path = "Code/Scan/scan.ino"
        fqbn = "esp32:esp32:esp32"
        
        if upload:
            upload_code(port, sketch_path, fqbn)
        else:
            monitor_serial(port)
    else:
        console.print("[red]Exiting due to no ESP32 device found.[/red]")

def run_check():
    check_connections()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile, upload, and monitor ESP32.")
    parser.add_argument('-u', '--upload', action='store_true', help='Compile and upload the sketch.')
    args = parser.parse_args()
    
    main(upload=args.upload)
