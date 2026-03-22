# CS50P – Problem Set 4: Libraries

My solutions to **Problem Set 4** of [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python).

---

## Problems

### 1. 😎 Emojize — `Emojize.py`
**Problem:** [cs50.harvard.edu/python/psets/4/emojize](https://cs50.harvard.edu/python/psets/4/emojize/)

Prompts the user for a string and converts any emoji aliases (e.g. `:thumbs_up:`) into their actual emoji using the `emoji` library.

**Install:**
```bash
pip install emoji
```

**Run:**
```bash
python Emojize.py
```
**Example:**
```
Input: I love Python :snake:
I love Python 🐍
```
```
Input: :thumbs_up: great work
👍 great work
```

---

### 2. 🅰️ Frank, Ian and Glen's Letters — `figlet.py`
**Problem:** [cs50.harvard.edu/python/psets/4/figlet](https://cs50.harvard.edu/python/psets/4/figlet/)

Converts text to ASCII art using the `pyfiglet` library. Supports optional `-f` or `--font` flag to specify a font. If no font is given, a random one is used.

**Install:**
```bash
pip install pyfiglet
```

**Run:**
```bash
python figlet.py                        # random font
python figlet.py -f slant               # specific font
python figlet.py --font banner          # specific font (long flag)
```
**Example:**
```
Input: Hello
 _   _      _ _
| | | | ___| | | ___
| |_| |/ _ \ | |/ _ \
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/
```

---

### 3. 👋 Adieu, Adieu — `adieu.py`
**Problem:** [cs50.harvard.edu/python/psets/4/adieu](https://cs50.harvard.edu/python/psets/4/adieu/)

Prompts the user for names one at a time (until EOF) and bids farewell to all of them using grammatically correct English via the `inflect` library.

**Install:**
```bash
pip install inflect
```

**Run:**
```bash
python adieu.py
```
**Example:**
```
Name: Alice
Name: Bob
Name: Charlie
Adieu, adieu, to Alice, Bob, and Charlie
```
```
Name: Alice
Name: Bob
Adieu, adieu, to Alice and Bob
```

---

### 4. 🎲 Guessing Game — `game.py`
**Problem:** [cs50.harvard.edu/python/psets/4/game](https://cs50.harvard.edu/python/psets/4/game/)

Prompts the user for a level `n` then generates a random integer between 1 and n. The user keeps guessing until they get it right, receiving "Too small" or "Too large" hints along the way.

**Run:**
```bash
python game.py
```
**Example:**
```
Level: 10
Guess: 5
Too small
Guess: 8
Too Big
Guess: 7
Just right
```

---

### 5. 🧮 Little Professor — `professor.py`
**Problem:** [cs50.harvard.edu/python/psets/4/professor](https://cs50.harvard.edu/python/psets/4/professor/)

Simulates a math quiz toy. Asks the user for a difficulty level (1–3), generates 10 random addition problems, gives up to 3 attempts per problem, shows `EEE` on wrong answers, reveals the correct answer after 3 failures, and prints a final score out of 10.

**Run:**
```bash
python professor.py
```
**Example:**
```
Level: 1
6 + 3 = 9
3 + 5 = 8
...
Score: 7
```

---

### 6. ₿ Bitcoin Price Index — `bitcoin.py`
**Problem:** [cs50.harvard.edu/python/psets/4/bitcoin](https://cs50.harvard.edu/python/psets/4/bitcoin/)

Takes a number of Bitcoins as a command-line argument and fetches the current Bitcoin price from the CoinCap API, then outputs the cost in USD formatted to 4 decimal places.

**Install:**
```bash
pip install requests
```

**Run:**
```bash
python bitcoin.py 1
python bitcoin.py 0.5
python bitcoin.py 10
```
**Example:**
```
$ 65,432.1234
```

---

## What I Learned
- Installing and using third-party libraries — `emoji`, `pyfiglet`, `inflect`, `requests`
- `sys.argv` for command-line arguments
- `EOFError` handling for end-of-input
- Fetching live data from APIs with `requests`
- Parsing JSON responses with `.json()`
- `random.randint()` for random number generation
- Error handling with `try/except` for `ValueError`, `requests.RequestException`
- f-string number formatting — `{cost:,.4f}`

---

## Course
**CS50's Introduction to Programming with Python**
Harvard University — [cs50.harvard.edu/python](https://cs50.harvard.edu/python)
