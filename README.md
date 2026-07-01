# 🐍 Snake Game (Python)

A classic Snake game built with Python's `turtle` module — my first project after learning Python basics.

## 💭 The Story

When I was a kid, I always got frustrated whenever the snake died from biting its own tail. So when I built this game myself, I decided to fix that childhood annoyance: **the snake can pass through itself without dying.** The only way to lose is hitting the wall.

## 🎮 Features

- Classic snake movement and growth
- Random food spawn with random shape (triangle/square) and color each round
- Live score and high score tracking
- Increasing speed as your score grows
- Fixed-size game window with a clean dark theme
- No self-collision death — snake can cross itself freely

## 🛠️ Built With

- Python 3
- [`turtle`](https://docs.python.org/3/library/turtle.html) — graphics
- `random` — food spawning
- `time` — game loop timing

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/snake-game-python.git
   cd snake-game-python
   ```
3. Run the game:
   ```bash
   python snake.py
   ```

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |

## 📌 Notes

- Hitting the wall resets the game (score returns to 0, high score is kept).
- Eating food increases your score by 10 and speeds up the snake slightly.

## 👩‍💻 Author

Created by **Menna Ayman**
