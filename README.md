# GeoBingo

GeoBingo is a terminal-based Bingo game written in Python.
The player answers capital city questions to reveal numbers on a 7×3 Bingo card.
If the revealed number is on the card, it is marked automatically.
You win by completing the card before running out of attempts.

## Features

* 7×3 Bingo card with unique random numbers (1–99)
* Country–capital questions loaded from a CSV file
* Automatic marking and win/loss detection
* Simple text interface in the terminal
* Basic unit tests for data and card validation

## Requirements

* Python 3.10 or higher
* Dependencies listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/<your-username>/geobingo.git
cd geobingo
pip install -r requirements.txt
```

## How to Run

```bash
python my_package/main.py
```

## How to Play

1. The game shows a country name.
2. Type its capital and press Enter.
3. If correct, the round’s number is revealed and marked if it appears on your card.
4. You win by completing the card; you lose when attempts reach zero.

## Tests

```bash
unittest
```

## Project Structure

```
data/          # CSV dataset (countries and capitals)
my_package/    # Game logic and configuration
tests/         # Unit tests
```

## License

See the LICENSE file for details.
