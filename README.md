# Password Manager (CLI)

A command-line password manager built in Python that encrypts stored credentials using industry-standard cryptography. Built as a hands-on project to learn practical encryption concepts for cybersecurity.

## Features

- **Master password protection** — one password unlocks access to all stored credentials
- **Encryption at rest** — all saved passwords are encrypted before being written to disk (nothing is ever stored in plain text)
- **Key derivation with salting** — the master password is never used directly as an encryption key; it's stretched using PBKDF2HMAC with a random salt and 390,000 iterations, making brute-force attacks significantly harder
- **Simple CLI menu** — add and view saved credentials through a straightforward terminal interface

## How it works

1. On first run, a random salt is generated and saved locally
2. Your master password + that salt are combined using PBKDF2 (a key derivation function) to produce a secure encryption key
3. Individual passwords are encrypted using **Fernet** (symmetric AES encryption) before being saved to `passwords.json`
4. To view a saved password, the same master password re-derives the key needed to decrypt it

## Security concepts demonstrated

- Symmetric encryption (AES via Fernet)
- Key derivation functions (PBKDF2HMAC) and why raw passwords should never be used as encryption keys directly
- Salting to prevent precomputed attacks (rainbow tables)
- Keeping sensitive data (salt, encrypted vault) out of version control via `.gitignore`

## Tech stack

- Python 3
- [`cryptography`](https://pypi.org/project/cryptography/) library

## Setup

```bash
git clone https://github.com/prashamsathapa-jpg/password-manager.git
cd password-manager
python3 -m venv venv
source venv/bin/activate
pip install cryptography
python3 main.py
```

## Usage
1 ADD password
2 VIEW password 
3 QUIT

Enter your master password once at startup, then use the menu to add or retrieve saved credentials.

## Planned improvements

- [ ] Hide password input while typing
- [ ] Add a "delete entry" option
- [ ] Add a password generator
- [ ] Handle incorrect master password gracefully

## Disclaimer


This is a learning project built to understand encryption fundamentals — it hasn't been security-audited and isn't recommended for storing real, sensitive credentials in production use.
