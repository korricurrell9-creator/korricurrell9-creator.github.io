# 🔍 ThreadPoolExecutor URL Collector

A fast, terminal‑based Python tool for **bulk URL inspection** using multithreading.  
Designed for **ethical security research**, automation, and analysis of web endpoints.

This script efficiently fetches multiple URLs in parallel, follows redirects, and records
response metadata for further inspection.

---

## ✨ Features

- 🚀 Multithreaded URL processing (ThreadPoolExecutor)
- 🔁 Follows redirects automatically
- 🧾 Captures HTTP status codes and final URLs
- 📄 Saves results to structured JSON
- 🛡️ TLS verification disabled for research environments
- 🧑‍💻 Fully CLI‑based, no GUI dependencies

---

## ⚠️ Ethical Use Notice

This tool is intended **only for authorized testing, learning, and research**.  
Do **not** scan systems you do not own or have permission to test.

You are responsible for complying with all applicable laws.

---

## 🛠️ Requirements

- Python **3.10+**
- Linux / macOS / WSL recommended

Python dependencies:
- `requests`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/korricurrell9-creator/ThreadPoolExecutor.git
cd ThreadPoolExecutor

