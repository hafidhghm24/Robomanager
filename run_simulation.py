import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from robot import Robot
from carte import create_map
from config import (
    NB_ROBOTS,
    TEMP_MIN,
    TEMP_MAX,
    BASE_X,
    BASE_Y,
    MAP_L,
    MAP_H,
    TICK_LIMIT,
    GIF_NAME,
)


def run_simulation():
    print("[Simulation] Start")
    world = create_map()
    robots = [Robot(i, world) for i in range(NB_ROBOTS)]

    cmap = plt.cm.get_cmap("coolwarm")
    norm = plt.Normalize(vmin=TEMP_MIN, vmax=TEMP_MAX)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(np.array(world), cmap=cmap, norm=norm)
    # show the base using a house emoji for better visibility
    ax.text(BASE_X, BASE_Y, "\U0001F3E0", fontsize=16, ha="center", va="center")
    robot_plot = ax.scatter([], [], s=120, marker="o", label="Robot")

    ax.set_xticks(range(MAP_L))
    ax.set_yticks(range(MAP_H))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color="gray", linestyle=":", linewidth=0.5)
    ax.legend(loc="upper right")

    active = {r.id: True for r in robots}

    def update(frame):
        xs, ys, colors = [], [], []
        still = 0
        for r in robots:
            if active[r.id]:
                if r.step():
                    still += 1
                else:
                    active[r.id] = False
            xs.append(r.x)
            ys.append(r.y)
            colors.append(r.color())
        robot_plot.set_offsets(np.c_[xs, ys])
        robot_plot.set_color(colors)
        ax.set_title(f"Tick {frame}")
        if still == 0 or frame >= TICK_LIMIT:
            anim.event_source.stop()
        return robot_plot,

    anim = animation.FuncAnimation(fig, update, interval=300, blit=True)
    plt.show()
    anim.save(GIF_NAME, writer=animation.PillowWriter(fps=4))
    for r in robots:
        r.save_csv()


if __name__ == "__main__":
    run_simulation()
