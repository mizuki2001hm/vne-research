# scripts/test_env.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.env.vne_env import VNEEnv

env = VNEEnv()
obs, info = env.reset()
print("初期状態:", obs)

for _ in range(3):
    action = env.action_space.sample()
    obs, reward, done, truncated, info = env.step(action)
    print(f"行動: {action}, 状態: {obs}, 報酬: {reward}, 割り当て成功: {info['assigned']}, done: {done}")

env.render()
