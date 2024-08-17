# Tools/check_port.py
import serial.tools.list_ports
from rich.console import Console

console = Console()

def check_connections():
    ports = serial.tools.list_ports.comports()
    if not ports:
        console.print("[red]No serial ports found.[/red]")
        return []

    console.print("[bold green]Detected serial ports:[/bold green]")
    detected_ports = []

    for port in ports:
        console.print(f"[cyan]Port:[/cyan] {port.device}")
        console.print(f"[cyan]Description:[/cyan] {port.description}")
        console.print(f"[cyan]Hardware ID:[/cyan] {port.hwid}")
        console.print()

        if 'Silicon Labs CP210x USB to UART Bridge' in port.description:
            detected_ports.append(port.device)
            console.print(f"[bold green]ESP32 detected on port {port.device}[/bold green]")
            break  # Exit after finding the first ESP32

    if not detected_ports:
        console.print("[red]No ESP32 device found.[/red]")

    return detected_ports
