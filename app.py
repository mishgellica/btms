from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "change_this_secret"
DB = "banking.db"

# ---------- Database helpers ----------

def get_db_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number TEXT UNIQUE,
            name TEXT NOT NULL,
            gender TEXT,
            nationality TEXT,
            balance REAL NOT NULL DEFAULT 0.0,
            status INTEGER NOT NULL DEFAULT 1,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Generates a human-friendly account number
def generate_account_number():
    return f"BS{random.randint(10000, 99999)}"

# ---------- Routes ----------

@app.route('/')
def index():
    return render_template('index.html')

# Open account 
@app.route('/open', methods=['GET', 'POST'])
def open_account():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        gender = request.form.get('gender', '').strip()
        nationality = request.form.get('nationality', '').strip()
        try:
            balance = float(request.form.get('balance', 0))
        except ValueError:
            flash('Invalid initial balance', 'error')
            return redirect(url_for('open_account'))

        if not name:
            flash('Name is required', 'error')
            return redirect(url_for('open_account'))

        account_number = generate_account_number()
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''INSERT INTO accounts (account_number, name, gender, nationality, balance, status, created_at)
                     VALUES (?, ?, ?, ?, ?, 1, ?)''',
                  (account_number, name, gender, nationality, balance, datetime.now().isoformat()))
        conn.commit()
        conn.close()

        flash(f'Account created: {account_number}', 'success')
        return redirect(url_for('index'))

    return render_template('open_account.html')

# All accounts 
@app.route('/accounts')
def all_accounts():
    conn = get_db_connection()
    accounts = conn.execute('SELECT * FROM accounts WHERE status = 1 ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('all_accounts.html', accounts=accounts)

# Deposit (GET: form, POST: perform deposit)
@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        acc = request.form.get('account_number', '').strip()
        try:
            amount = float(request.form.get('amount', 0))
        except ValueError:
            flash('Invalid amount', 'error')
            return redirect(url_for('deposit'))

        if amount <= 0:
            flash('Amount must be positive', 'error')
            return redirect(url_for('deposit'))

        conn = get_db_connection()
        c = conn.cursor()
        row = c.execute('SELECT * FROM accounts WHERE account_number = ? AND status = 1', (acc,)).fetchone()
        if not row:
            conn.close()
            flash('Account not found or closed', 'error')
            return redirect(url_for('deposit'))

        c.execute('UPDATE accounts SET balance = balance + ? WHERE account_number = ?', (amount, acc))
        conn.commit()
        conn.close()
        flash(f'₱{amount:.2f} deposited to {acc}', 'success')
        return redirect(url_for('index'))

    return render_template('deposit.html')

# Withdraw
@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        acc = request.form.get('account_number', '').strip()
        try:
            amount = float(request.form.get('amount', 0))
        except ValueError:
            flash('Invalid amount', 'error')
            return redirect(url_for('withdraw'))

        if amount <= 0:
            flash('Amount must be positive', 'error')
            return redirect(url_for('withdraw'))

        conn = get_db_connection()
        c = conn.cursor()
        row = c.execute('SELECT * FROM accounts WHERE account_number = ? AND status = 1', (acc,)).fetchone()
        if not row:
            conn.close()
            flash('Account not found or closed', 'error')
            return redirect(url_for('withdraw'))

        if row['balance'] < amount:
            conn.close()
            flash('Insufficient balance', 'error')
            return redirect(url_for('withdraw'))

        c.execute('UPDATE accounts SET balance = balance - ? WHERE account_number = ?', (amount, acc))
        conn.commit()
        conn.close()
        flash(f'₱{amount:.2f} withdrawn from {acc}', 'success')
        return redirect(url_for('index'))

    return render_template('withdraw.html')

# Close account 
@app.route('/close/<account_number>', methods=['POST'])
def close_account(account_number):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('UPDATE accounts SET status = 0 WHERE account_number = ?', (account_number,))
    conn.commit()
    conn.close()
    flash('Account closed (soft delete)', 'success')
    return redirect(url_for('index'))


# Close page for listing and closing accounts
@app.route('/close_accounts')
def close_accounts():
    conn = get_db_connection()
    accounts = conn.execute('SELECT * FROM accounts WHERE status = 1 ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('close_account.html', accounts=accounts)

# Closed accounts
@app.route('/closed_accounts')
def closed_accounts():
    conn = get_db_connection()
    accounts = conn.execute(
        'SELECT * FROM accounts WHERE status = 0 ORDER BY id DESC'
    ).fetchall()
    conn.close()
    return render_template('closed_accounts.html', accounts=accounts)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)