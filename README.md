# 🛡️ Containerized Security Toolkit

A lightweight, fully isolated Docker environment packed with essential network auditing tools. 

## 📖 The Problem
Onboarding a new IT team member or coordinating an external security audit often takes hours just to install, configure, and resolve dependency conflicts for network testing tools across different operating systems.

## 💡 The Solution
This repository provides a reproducible environment using Alpine Linux. It comes pre-loaded with `nmap`, `sqlmap`, and a custom Python automation script. **You do not need to install any security tools on your host machine—just Docker.**

### 🚀 Quick Start

**1. Build the Image:**
Clone this repository and build the Docker image (this takes less than a minute):
```bash
docker build -t sec-toolkit .