# GeoBingo

**GeoBingo** is an educational, terminal-based Bingo game written in Python.  
The player answers capital city questions to reveal numbers on a 7×3 Bingo card.  
If the revealed number appears on the card, it is automatically marked.  
You win by completing the entire card before running out of attempts!

---

## Features

- 7×3 Bingo card with unique random numbers (1–99)  
- Country–capital questions loaded dynamically from a CSV file  
- Random, non-repeating capital questions  
- Multiple difficulty levels (e.g., World / Europe)  
- Automatic number marking and win/loss detection  
- Clear terminal interface with visual number crossing  
- On-screen instructions for easy gameplay  
- Basic unit tests for data validation and grid generation  

---

## Requirements

- Python **3.10** or higher  
- Dependencies listed in `requirements.txt`

---

## Installation

```bash
git clone https://github.com/annaymbern/GeoBingo.git
cd GeoBingo
pip install -r requirements.txt
```
---
## How to Run

python my_package/main.py


## How to Play
1. The game displays a country name.

2. Type its capital city and press Enter.

3. If your answer is correct:

- A random Bingo number is revealed.

- If that number is on your card, it is crossed out automatically.

4. The game ends when:

- You complete your card (you win), or

- You run out of attempts (you lose).

## Running tests
python -m unittest discover tests


## License

This project is licensed under the terms of the MIT License.
See the LICENSE file for details.

## Authors:
Developed collaboratively by the GeoBingo team as part of a learning project using the Scrum methodology; Anna Ymbern, Anna Espelt, Patricia Cerda, Helena Collart, Silvia Nueno, Jana Biosca.



