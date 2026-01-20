# 🔐 PyGenPass

Hey there! Need to create some rock-solid passwords without the hassle? You're in the right place.

**PyGenPass** is a simple Python script that helps you generate strong, randomized passwords—and you get to call the shots on exactly how they look. Lowercase? Uppercase? Numbers? Symbols? You pick. It's like having your own personal password factory.

---

## Why You'll Love PyGenPass

Let's be real—coming up with strong passwords is a pain. Most of us end up reusing the same ones (we've all been there). PyGenPass takes that burden off your shoulders:

- **You're in control** — Choose exactly what goes into your passwords
- **Generate as many as you need** — One password or a hundred, it's up to you
- **Random lengths** — Set a range, and each password gets a random length within it
- **Saves them for you** — All your passwords get saved to a `passwords.txt` file automatically

---

## Getting Started

### What You'll Need

Just Python 3. That's it. No extra libraries to install—everything uses Python's built-in modules.

### Running PyGenPass

1. **Download** the `Password generator.py` file
2. **Open your terminal** and navigate to where you saved it
3. **Run it:**
   ```bash
   python "Password generator.py"
   ```

That's all there is to it.

---

## How PyGenPass Works

Once you run the script, it'll walk you through a few quick questions:

### 1. How many passwords?
Tell it how many you want. One? Ten? Go wild.

### 2. Set your length range
Pick a minimum length (at least 6 characters—anything less isn't really secure) and a maximum. Each password will be a random length somewhere in between.

### 3. Choose your character types
PyGenPass asks you yes or no for each:
- **Lowercase letters** (a-z)
- **Uppercase letters** (A-Z)
- **Digits** (0-9)
- **Symbols** (!@#$%^&*)

Just make sure you pick at least one—otherwise, there's nothing to build a password from!

### 4. Get your passwords
PyGenPass generates them right away, shows you each one with its length, and saves everything to `passwords.txt`.

---

## Example Run

Here's what a typical session looks like:

```
============================================================
              🔐 Strong Password Generator 🔐
============================================================

How many passwords do you want to be made? 5
Minimum password length (at least 6): 12
Maximum password length (at least 12): 16

Include lowercase letters? (yes/no): yes
Include uppercase letters? (yes/no): yes
Include digits? (yes/no): yes
Include symbols? (yes/no): yes

============================================================
                 🎉 Generated Passwords 🎉
============================================================
1. kP4@mNq2#xYz (length: 12)
2. Bg7%tRs&Wv5Lp (length: 13)
3. zA9*dFh!jK3mQr (length: 14)
4. Xy2#nBv$cM8pLq6 (length: 15)
5. wE5@gHj&sD4kMn7! (length: 16)

✅ Passwords have been saved to 'passwords.txt'
```

---

## Under the Hood

If you're curious about how PyGenPass works:

- **`generate_password()`** — The heart of the operation. Takes your preferences and spits out a randomized password using Python's `random.choice()`.

- **`get_yes_no()`** — Handles all those yes/no questions and makes sure you actually give a valid answer.

- **`get_number()`** — Asks for numbers and keeps you honest about minimum values.

PyGenPass builds a pool of characters based on your choices, then randomly picks from that pool to create each password. Simple, but effective.

---

## Quick Tips

- **Longer is generally better** — A 16-character password is way harder to crack than an 8-character one
- **Mix it up** — Using all four character types makes your passwords significantly stronger
- **Check your file** — Remember, passwords get *appended* to `passwords.txt`, so you won't lose old ones if you run PyGenPass again

---

## What's Inside

| File | What It Does |
|------|--------------|
| `Password generator.py` | The main PyGenPass script—run this |
| `passwords.txt` | Where your generated passwords end up |

---

## A Few Notes

- PyGenPass uses Python's `random` module, which is great for general use. If you need cryptographically secure passwords for highly sensitive stuff, you might want to swap it out for `secrets` instead.
- Passwords are saved in plain text, so keep that file somewhere safe!

---

## Need to Tweak Something?

Feel free to dive into the code and make it your own. Want different symbols? Change the `!@#$%^&*` string. Want a different default minimum length? Adjust the `6` in the `get_number()` call. It's your tool now.

---

**PyGenPass** — Made with ☕ and a healthy distrust of "password123"