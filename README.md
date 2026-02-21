# Linux Local Enumeration Script

## Description

This Python script performs basic local enumeration on a Linux system.
It gathers useful information that can help during privilege escalation or system analysis.

The goal of this project is to understand:

- User context
- Kernel information
- Open ports
- Running processes

This script is part of my cybersecurity learning journey.

---

## Features:

The script collects:

### User information
- `whoami`
- `id`

### Kernel information
- `uname -a`

### Open ports
- `ss -tuln`

### Running processes
- `ps aux | head -n 10`

---

## Usage

Clone the repository and run the script:
```bash
git clone https://github.com/sosec11/linux-local-enum.git
cd linux-local-enum

python3 linux-local-enum.py