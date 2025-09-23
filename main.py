
import time
import random
import math
import sys
import curses

class ASCIICanvas:
    def __init__(self, width=60, height=30):
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        self.buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def draw_point(self, x, y, char='*'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[int(y)][int(x)] = char

    def draw_line(self, x1, y1, x2, y2, char='#'):
        points = self._get_line_points(x1, y1, x2, y2)
        for x, y in points:
            self.draw_point(x, y, char)

    def _get_line_points(self, x1, y1, x2, y2):
        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        
        while True:
            points.append((x1, y1))
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
        return points

    def render(self):
        return '\n'.join([''.join(row) for row in self.buffer])

class AnimationEngine:
    def __init__(self):
        self.canvas = ASCIICanvas()
        self.particles = []
        self.time = 0
        self.palette = ['@', '#', '*', '+', ':', '.', ' ']

    def add_particle(self, x, y, vx, vy, life):
        self.particles.append({
            'x': x, 'y': y, 
            'vx': vx, 'vy': vy,
            'life': life,
            'max_life': life,
            'char': random.choice(self.palette)
        })

    def update(self):
        self.time += 0.1
        self.canvas.clear()

        # Update particles
        for p in self.particles[:]:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['life'] -= 1
            if p['life'] <= 0:
                self.particles.remove(p)
            else:
                alpha = p['life'] / p['max_life']
                self.canvas.draw_point(p['x'], p['y'], p['char'])

        # Add new particles
        if random.random() < 0.3:
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.5, 2)
            self.add_particle(
                self.canvas.width // 2,
                self.canvas.height // 2,
                math.cos(angle) * speed,
                math.sin(angle) * speed,
                random.randint(20, 50)
            )

        # Draw some animated shapes
        size = 10 + 5 * math.sin(self.time)
        self._draw_rotating_square(size)
        self._draw_wave_text("ASCII ART", 5, 15)

    def _draw_rotating_square(self, size):
        angle = self.time
        points = []
        for i in range(4):
            x = self.canvas.width // 2 + size * math.cos(angle + i * math.pi / 2)
            y = self.canvas.height // 2 + size * math.sin(angle + i * math.pi / 2)
            points.append((x, y))
        
        for i in range(4):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % 4]
            self.canvas.draw_line(x1, y1, x2, y2, '#')

    def _draw_wave_text(self, text, x, y):
        for i, c in enumerate(text):
            wave_y = y + 3 * math.sin(self.time + i * 0.5)
            self.canvas.draw_point(x + i, wave_y, c)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    engine = AnimationEngine()

    while True:
        engine.update()
        stdscr.clear()
        stdscr.addstr(0, 0, engine.canvas.render())
        stdscr.refresh()

        # Handle input
        try:
            key = stdscr.getch()
            if key == ord('q'):
                break
            elif key == ord(' '):
                # Add explosion
                for _ in range(30):
                    angle = random.uniform(0, 2 * math.pi)
                    speed = random.uniform(1, 3)
                    engine.add_particle(
                        engine.canvas.width // 2,
                        engine.canvas.height // 2,
                        math.cos(angle) * speed,
                        math.sin(angle) * speed,
                        random.randint(30, 60)
                    )
        except:
            pass

        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(main)
