# Asteroids Game

A simple Asteroids clone built with Python and Pygame.

## Features
- Player ship that rotates and moves
- Asteroids spawn and move across the screen
- Player can shoot bullets
- Collision detection between player and asteroids
- Sprite groups for efficient updates and drawing

## Controls
- **A / D**: Rotate ship left/right
- **W / S**: Move ship forward/backward
- **Spacebar**: Shoot bullets
- **Esc / Close Window**: Quit game

## Requirements
- Python 3.8+
- Pygame

## Setup
1. Install Python and Pygame:
   ```bash
   pip install pygame
   ```
2. Run the game:
   ```bash
   python main.py
   ```

## File Structure
- `main.py` — Game loop and initialization
- `player.py` — Player ship logic
- `asteroid.py` — Asteroid logic
- `asteroidfield.py` — Asteroid spawning
- `shot.py` — Bullet logic
- `circleshape.py` — Base class for circular sprites
- `constants.py` — Game constants

## To Do
- Add bullet-asteroid collision
- Add score and lives
- Add sound effects

---
Enjoy blasting asteroids!
