# Asteroids Game

A small Asteroids clone built with Python and Pygame.

## Features
- Player ship that rotates and moves
- Asteroids spawn and move across the screen
- Player can shoot bullets
- Collision detection between player and asteroids
- Sprite groups for efficient updates and drawing
- Shield power-up: pick up a shield to become invulnerable for a short time
- HUD timer: remaining shield time is shown under the score while active

## Controls
- A / D: Rotate ship left/right
- W / S: Move ship forward/backward
- Spacebar: Shoot bullets
- Esc / Close Window: Quit game

## Requirements
- Python 3.12 (project pyproject.toml targets >=3.12)
- Pygame (see pinned version in pyproject.toml)

## Setup
1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies (pyproject pins pygame):
   ```bash
   pip install -r <(python - <<'PY'
import tomllib, sys
pyproject = tomllib.loads(open('pyproject.toml','rb').read())
deps = pyproject.get('project',{}).get('dependencies', [])
print('\n'.join(d for d in deps))
PY
)
   ```
   Or simply:
   ```bash
   pip install pygame==2.6.1
   ```
3. Make sure you have a background image named `asteroids_background.jpg` in the project folder.
4. Run the game:
   ```bash
   python main.py
   ```

## Power-up details
- Shield: spawns periodically (see `POWERUP_SPAWN_RATE` in `constants.py`).
- Picking up a shield sets a timer (see `SHIELD_DURATION`) and grants temporary invulnerability; the remaining time is displayed in the HUD.

## Configurable constants
You can tweak spawn rates and durations in `constants.py`:
- `SHIELD_DURATION` — how long the shield lasts (seconds).
- `POWERUP_SPAWN_RATE` — approximate seconds between power-up spawns.
- `SHIELD_RADIUS` — visual radius for the power-up pickup.

## File Structure (high level)
- `main.py` — Game loop and HUD rendering
- `player.py` — Player ship, shooting, and shield handling
- `asteroid.py` — Asteroid logic and splitting
- `asteroidfield.py` — Spawning of asteroids and power-ups
- `powerup.py` — Power-up sprite (shield)
- `shot.py` — Bullet logic
- `circleshape.py` — Base class for circular sprites
- `constants.py` — Game constants (sizes, speeds, power-up values)
- `asteroids_background.jpg` — Background image for the game

## Roadmap / Planned Features
- Multiple lives and respawning
- Player acceleration
- Screen wrap-around for all objects
- Different weapon types
- Sound effects

---
Enjoy blasting asteroids!
