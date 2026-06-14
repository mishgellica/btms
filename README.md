# BTMS: Easy Banking | Bank Operations 

A straightforward banking program built in Python that lets users handle everyday account tasks like opening a brand new account, adding money, making withdrawals, and checking their current balance on the fly.

Built as a backend logic project by Bai Fatima Andong, Christian James Cahilig, Karylle Mish Gellica, Daniel Cott Gerarman, Jan Loren Odiong, and John Llorie Sarmiento, University of Mindanao.

---

## What This Does

This application provides a text-based interface to simulate essential retail banking operations directly inside a terminal window. 

You can interactively step through a customer lifecycle — registering a brand new user profile, funding the account via deposit inputs, executing real-time withdrawals, and checking transactional balances. The core terminal runtime performs data evaluations instantly behind the scenes, ensuring numbers balance dynamically without data decay.

---

## The Core Features Breakdown

- **Account Lifecycle Creation:** Instantly provisions a unique account instance tied to a user profile setup.
- **Transactional Balances:** Handles account funding through numerical deposit pipelines.
- **Safe Withdrawal Logic:** Evaluates active financial ledgers to block overdraft attempts on the fly.
- **Strict Input Validation:** Enforces zero-boundary parameters to completely block negative numeric inputs.
- **Centralized Data Representation:** Employs Object-Oriented Programming principles to track customer details securely in memory.

---

## The Problem and Solution

### Core Problem
Managing everyday personal banking or tracking transactions using paper records or scattered files is slow, prone to math mistakes, and lacks a simple way to instantly verify if an account actually has enough funds before a withdrawal. 

### Core Solution
Created a unified Python command line system that models real-world account structures using code logic. It handles deposits and withdrawals safely by instantly checking available balances, enforces strict validation to block negative numeric inputs, and keeps customer details updated in a central data setup.

---

## Installing and Running Locally

Follow these steps to run the project on your own computer.

### What You'll Need First

Make sure you have these installed before starting:

- **Python 3.x** — Download from [python.org](https://www.python.org/downloads/). During installation on Windows, tick **"Add Python to PATH"**.
- **Git** — Download from [git-scm.com](https://git-scm.com/downloads).

To check if they're installed, open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:
python --version
git --version

Both should print a version number. If they do, you're ready.

---

### Step 1 — Clone the Repository

This downloads a copy of the project to your computer:
git clone https://github.com/mishgellica/btms.git
cd btms

---

### Step 2 — Create a Virtual Environment

This keeps the project's configurations separate from the rest of your system:

python -m venv .venv

Now activate it:

**Windows:**
.venv\Scripts\activate

**Mac/Linux:**
source .venv/bin/activate

You'll know it worked when `(.venv)` appears at the start of your terminal prompt.

---

### Step 3 — Run the App

Since this system functions as a pure backend engine layout using native Python logic tools, it runs natively inside your command shell without extra library dependencies:
python main.py


*(Note: Replace `main.py` with the specific entry point script name of the repository if it uses a different filename).*

---

## Tech Stack

- **Execution Engine:** Python 3.x
- **Programming Paradigm:** Object-Oriented Programming (OOP) Logic
- **Interface Structure:** Command Line Interface (CLI)

---

## Limitations

- **Volatile In-Memory Storage:** The system holds data structures in active runtime storage, meaning account indices reset to default once the console application process exits.
- **Console Environment Constraints:** Operations rely entirely on textual command parsing inputs instead of an interactive web browser interface dashboard.
- **Single-Currency Metrics:** Transactions run under basic numerical values without handling currency conversions or international formatting configurations.

---

## Authors

**Bai Fatima A. Andong** — b.andong.545438@umindanao.edu.ph  
**Christian James C. Cahilig** — c.cahilig.544797@umindanao.edu.ph  
**Karylle Mish T. Gellica** — k.gellica.544337@umindanao.edu.ph  
**Daniel Cott Gerarman** — d.gerarman.546010@umindanao.edu.ph
**Jan Loren Odiong** — j.odiong.544579@umindanao.edu.ph
**John Llorie Sarmiento** — j.sarmiento.545495@umindanao.edu.ph
BS Computer Science, University of Mindanao — Final Project, 2026

---

## License

This project is for academic and educational purposes only.
