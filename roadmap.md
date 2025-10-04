qFuture improvements...

Scoring System: Add a score variable in main.py. Increase score when an asteroid is destroyed. Display it on the screen using pygame.font.
Multiple Lives & Respawning: Add a lives counter. When the player collides with an asteroid, decrease lives and respawn the player at the center.
Asteroid Explosion Effect: Create an Explosion sprite/class. Spawn it at the asteroid’s position when split/kill is called. Animate and remove after a short time.
Player Acceleration: Add a velocity vector to the player. On pressing forward, increase velocity by an acceleration value, then update position by velocity.
Screen Wrapping: In each sprite’s update, if position goes off-screen, wrap to the opposite edge.
Background Image: Load an image with pygame.image.load and blit it before drawing sprites.
Weapon Types: Add a variable for weapon type in Player. Change firing logic based on type (spread, rapid, bombs, etc.).
Lumpy Asteroids: Generate random points around a circle for each asteroid, then draw a polygon instead of a circle.
Triangular Ship Hitbox: Override collision logic for the player to use the triangle points instead of a radius.
Shield Power-up: Create a Shield sprite/power-up. When collected, prevent player death for a time.
Speed Power-up: Create a Speed power-up. When collected, temporarily increase player acceleration/speed.
Bombs: Add a bomb weapon type. When dropped, create a large explosion that destroys nearby asteroids.