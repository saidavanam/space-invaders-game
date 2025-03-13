# Space Invaders 🚀  

A simple **Space Invaders** game built with **Python 3.11.7** and **Pygame 2.6.0**. Enjoy the classic arcade experience by running `space_invaders.py`!  

---

## 🎮 How to Play  
Run the **`space_invaders.py`** file and enjoy the game!  

```bash
python space_invaders.py
```

Use the following controls:
- **Left Arrow (←):** Move left
- **Right Arrow (→):** Move right
- **Spacebar:** Fire bullets
- **Close Button:** Exit the game

---

## ⚙️ Requirements  
- **Python**: 3.11.7  
- **Pygame**: 2.6.0  

Install dependencies using:  
```bash
pip install pygame
```

---

## 🔧 Game Features & Customizations  

### 1️⃣ Adjust Enemy Speed  
Modify `enemyXchange` and `enemyYchange` values to tweak enemy movement:  
```python
enemyXchange.append(2)  
enemyYchange.append(40)  # Try different values
```

### 2️⃣ Change Background Music  
Replace the background music file:  
```python
mixer.music.load('background.wav')
```

### 3️⃣ Set a Custom Background  
Change the game’s background image:  
```python
background = pygame.image.load('space_background.jpg')
```

### 4️⃣ Bullet Sound Effects  
Modify the bullet firing sound:  
```python
bullet_sound = mixer.Sound('laser.wav')
```

### 5️⃣ Explosion Sound (When Bullet Hits Invader)  
Customize the explosion sound effect:  
```python
explosion_sound = mixer.Sound('explosion.wav')
```

### 6️⃣ Displaying a Boundary at 440px  
If you want to **show a boundary** at `y = 440`, you can draw a line:  
```python
pygame.draw.line(screen, (255, 0, 0), (0, 440), (800, 440), 2)  # Red boundary line
```

---

## 📜 Game Code Summary  
### Player Setup  
```python
player1img = pygame.image.load('player1.png')
player1X = 370
player1Y = 480
player1Xchange = 0
```

### Enemy Setup  
```python
enemies = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_enemies = 6

for i in range(num_enemies):
    enemies.append(pygame.image.load('enemy1.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 80))
    enemyXchange.append(2)
    enemyYchange.append(40)
```

### Bullet Firing Mechanism  
```python
def fire_bullet(x, y):
    bullets.append([x + 16, y])  # Fire from player’s position
```

### Collision Detection  
```python
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2) ** 0.5
    return distance < 27
```

### Game Over Condition  
```python
if enemyY[i] > 440:
    for j in range(num_enemies):
        enemyY[j] = 2000  # Move enemies out of the screen
    game_over_text()
```

---

## 🎯 Game Objective  
- Eliminate **all enemy invaders** before they reach the bottom!
- **Avoid collisions** and keep your score increasing.
- Have fun playing **Space Invaders!** 🚀👾

---

## 🛠 Future Enhancements  
- Add **multiple levels** with increasing difficulty.
- Introduce **power-ups** for the player.
- Implement a **leaderboard** to track high scores.

### 🔥 Enjoy playing Space Invaders! 🚀

