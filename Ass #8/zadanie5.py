import tkinter as tk

def read_pattern(file_path):
    with open(file_path, 'r') as file:
        size = int(file.readline())
        pattern = [list(map(int, file.readline().split())) for _ in range(size)]
    return size, pattern

def find_largest_empty_rectangle(size, pattern):
    max_area = 0
    left = 0
    right = 0
    height = [0] * size

    for i in range(size):
        for j in range(size):
            if pattern[i][j] == 0:
                height[j] += 1
            else:
                height[j] = 0

        stack = []
        for j in range(size + 1):
            while stack and (j == size or height[j] < height[stack[-1]]):
                h = height[stack.pop()]
                w = j if not stack else j - stack[-1] - 1
                if h * w > max_area:
                    max_area = h * w
                    left = stack[-1] + 1 if stack else 0
                    right = j - 1

            stack.append(j)

    return max_area, left, right

def draw_pattern_with_rectangle(size, pattern, left, right):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=size*20, height=size*20)
    canvas.pack()

    for i in range(size):
        for j in range(size):
            color = 'black' if pattern[i][j] == 1 else 'white'
            canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill=color)

    if left is not None and right is not None:
        for i in range(left, right+1):
            canvas.create_rectangle(i*20, 0, (i+1)*20, size*20, outline='red', width=2)

    root.mainloop()

if __name__ == "__main__":
    file_path = "zadanie5_input.txt"
    size, pattern = read_pattern(file_path)
    area, left, right = find_largest_empty_rectangle(size, pattern)
    print(f"Largest Empty Rectangle Area: {area}")
    draw_pattern_with_rectangle(size, pattern, left, right)
