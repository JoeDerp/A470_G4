import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle


# Constants
fig, ax = plt.subplots()
ax.set_xlim(-20, 5)
ax.set_ylim(-1, 20)
particle = Circle((0, 0), radius=0.1, fc='red')
ax.add_patch(particle)

total_frames = 100  # Total number of frames for the animation
stop_at_frame = 50  # Stop the animation at this frame

# Animation function
def animate(frame):
    x, y = particle.center
    print(frame)
    if frame >= stop_at_frame:  # Stop the animation when the frame reaches stop_at_frame
        anim.event_source.stop()
    else:
        particle.center = (x - 0.1, y)
    return particle,

# Create animation
anim = FuncAnimation(fig, animate, frames=total_frames, interval=2, blit=True)

# Save animation as GIF using Pillow writer

anim.save('particle_animation.gif', writer='pillow', fps=20)

plt.show()
