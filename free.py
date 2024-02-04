import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fps = 60.0
speed = 0.3

# カスタム関数を定義
def base_wave(x, t):
    condition = (x <= 6) & (x <= (2 + 7 * t))
    freq = 2 * np.pi * 7 / 4
    result = np.where(condition, np.sin(freq * (t - (x - 2) / 7)), 0)
    return result

def reflection(x, t):
    condition = (x <= 6) & (x >= (10 - 7 * t))
    freq = 2 * np.pi * 7 / 4
    result = np.where(condition, np.sin(freq * (t - (x - 2) / 7)), 0)
    return result

fig, ax1 = plt.subplots()
fig.set_size_inches(10, 8)
ax1.set_xlim(0, 10)
ax1.set_ylim(-2.2, 2.2)

line1, = ax1.plot([], [], 'b', lw=2, label='incident')
line2, = ax1.plot([], [], 'r', lw=2, label='reflection')
line3, = ax1.plot([], [], 'g', lw=1, label='composition')

# フレームの更新関数を定義
def update(frame):
    speed_frame = frame * speed
    t = ((speed_frame / fps) - 2/7)
    x_min1 = 0
    x_max1 = 6
    x1 = np.linspace(x_min1, x_max1, 1000)
    y1 = base_wave(x1, t)

    x_min2 = 0
    x_max2 = 6
    x2 = np.linspace(x_min2, x_max2, 1000)
    y2 = reflection(x2, t)

    x3 = x1
    y3 = base_wave(x3, t) + reflection(x3, t)
    line1.set_data(x1, y1)
    line2.set_data(x2, y2)
    line3.set_data(x3, y3)
    ax1.set_title(f'Frame {frame + 1}/{num_frames}  {t:.02f}[s]')

# アニメーションのフレーム数を設定
num_frames = int((1 + 2/7) * fps / speed)

# アニメーションを作成
animation = FuncAnimation(fig, update, frames=num_frames, interval=1/fps, repeat=False)

# 凡例を表示
lines = [line1, line2, line3]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels)

# アニメーションを表示
plt.show()
