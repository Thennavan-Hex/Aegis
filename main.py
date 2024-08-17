import argparse
from rich.console import Console
from rich.panel import Panel
import pyfiglet
import sys

# Import scan module from Tools directory
sys.path.insert(0, 'Tools')
import scan 

console = Console()

def show_banner():
    banner = pyfiglet.figlet_format("Aegis", font="epic")
    panel = Panel(banner, title="Aegis CLI", subtitle="Professional Network Operations Tool", style="bold blue", expand=False)
    console.print(panel, justify="center")

def show_version():
    console.print("[bold purple]Tool Version 1.0.0[/bold purple]", justify="center")

def setup_parser():
    parser = argparse.ArgumentParser(description="Aegis CLI - Professional Network Operations Tool")
    
    parser.add_argument("-v", "--version", action="version", version="Aegis CLI Version 1.0.0")
    parser.add_argument("command", nargs="?", choices=["scan", "check"], help="Command to run", default=None)
    parser.add_argument("-u", "--upload", action="store_true", help="Upload code to the detected device")
    return parser

def main():
    show_banner()
    parser = setup_parser()
    args = parser.parse_args()

    if args.command == "scan":
        scan.main(upload=args.upload)
    elif args.command == "check":
        scan.run_check()
    elif args.command is None:
        show_version()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
