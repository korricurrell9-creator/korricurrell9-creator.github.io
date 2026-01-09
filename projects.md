---
layout: page
title: Projects
---

# 🛠️ Korri’s Lab Projects

<section class="main-content">

Professional, terminal-first tools for **ethical security testing** and **automation**.

---

## 🚀 ThreadPoolExecutor Scanner

A multithreaded Python URL scanner designed for fast reconnaissance of web endpoints.  
Built for **ethical hacking, lab testing, and research**.

### ✨ What it does
- Sends concurrent HTTP requests to multiple URLs
- Follows redirects automatically
- Captures status codes and response previews
- Outputs structured JSON results
- Handles broken TLS certificates (common on VPN portals)

### 🧰 Tech
- Python 3.9+
- `requests`
- `ThreadPoolExecutor`
- CLI-only (no GUI)

### 📦 Installation

```bash
git clone https://github.com/korricurrell9-creator/korricurrell9-creator.github.io.git
cd korricurrell9-creator.github.io

python3 -m venv venv
source venv/bin/activate
pip install requests
python tools/threadpool_executor.py

