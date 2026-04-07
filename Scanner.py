#!/usr/bin/env python3
import argparse
import subprocess
import os
import datetime

def run_nmap_scan(target, output_dir):
    """Runs a comprehensive nmap scan and saves the output."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"nmap_audit_{target}_{timestamp}.txt")
    
    print(f"[*] Starting security audit on target: {target}")
    print("[*] Running NMAP (Service Detection & Default Scripts)...")
    
    # nmap flags: -sV (service versions), -sC (default safe scripts), -Pn (skip ping)
    nmap_cmd = ["nmap", "-sV", "-sC", "-Pn", target, "-oN", output_file]
    
    try:
        # Run the command and wait for it to finish
        subprocess.run(nmap_cmd, check=True)
        print(f"[+] Scan complete! Report saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running nmap: {e}")
    except FileNotFoundError:
        print("[-] nmap is not installed or not in PATH.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Security Toolkit Wrapper")
    parser.add_argument("target", help="The target IP address or hostname to scan")
    
    args = parser.parse_args()
    
    # The /reports directory matches the one created in our Dockerfile
    # This is critical for the volume mount to work correctly
    report_directory = "/reports"
    
    run_nmap_scan(args.target, report_directory)