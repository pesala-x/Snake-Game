import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"

        self.food = self.create_food()
        self.score = 0

        self.master.bind("<Key>", self.on_key_press)

        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")

    def move_snake(self):
        head = list(self.snake[0])

        if self.direction == "Up":
            head[1] -= 10
        elif self.direction == "Down":
            head[1] += 10
        elif self.direction == "Left":
            head[0] -= 10
        elif self.direction == "Right":
            head[0] += 10

        self.snake.insert(0, tuple(head))

        if self.snake[0] == self.canvas.coords(self.food):
            self.score += 1
            self.canvas.delete(self.food)
            self.food = self.create_food()
        else:
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

        self.draw_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")

    def on_key_press(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            if (key == "Up" and self.direction != "Down" or
                    key == "Down" and self.direction != "Up" or
                    key == "Left" and self.direction != "Right" or
                    key == "Right" and self.direction != "Left"):
                self.direction = key

    def update(self):
        self.move_snake()

        if self.check_collision():
            self.game_over()
        else:
            self.master.after(100, self.update)

    def check_collision(self):
        head = self.snake[0]
        x, y = head
        return (
                x < 0 or x >= 400 or
                y < 0 or y >= 400 or
                head in self.snake[1:]
        )

    def game_over(self):
        self.canvas.create_text(200, 200, text=f"Game Over. Score: {self.score}", fill="white", font=("Helvetica", 16))

# Create the Tkinter window
root = tk.Tk()
snake_game = SnakeGame(root)
root.mainloop()
