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
2. Make sure you have a background image named `asteroids_background.jpg` in the project folder. You can use your own image or the provided one.
3. Run the game:
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
- `asteroids_background.jpg` — Background image for the game

## Roadmap / Planned Features
- Multiple lives and respawning
- Player acceleration
- Screen wrap-around for all objects
- Different weapon types
- Lumpy asteroids (polygonal shapes)
- Triangular ship hitbox
- Shield power-up
- Speed power-up
- Bombs
- Sound effects

---
Enjoy blasting asteroids!
