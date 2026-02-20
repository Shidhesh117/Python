import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
lines = []
# Define strokes for B
b_strokes = [
 ([1, 1], [2, 8]),
 ([1, 3], [8, 7]),
 ([3, 1], [7, 6]),
 ([1, 3], [6, 5]),
 ([3, 1], [5, 2]),
]
# Define strokes for M
m_strokes = [
 ([4, 4], [2, 8]),
 ([4, 5], [8, 5]),
 ([5, 6], [5, 8]),
 ([6, 6], [8, 2]),
]
# Define strokes for S
s_strokes = [
 ([8, 10], [8, 8]),
 ([8, 8], [8, 5]),
 ([8, 10], [5, 5]),
 ([10, 10], [5, 2]),
 ([10, 8], [2, 2]),
]
# Combine all strokes
all_strokes = b_strokes + m_strokes + s_strokes
# Create invisible lines first
for stroke in all_strokes:
 line, = ax.plot([], [], lw=3)
 lines.append(line)
 
 
# Define animation function
def animate(i):
 if i < len(lines):
   lines[i].set_data(all_strokes[i][0], all_strokes[i][1])
 return lines
 
 
ani = animation.FuncAnimation(fig, animate, frames=len(lines) + 10,
interval=300, blit=True)

plt.show()
