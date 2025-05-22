# src/env/vne_env.py

import gymnasium as gym
import numpy as np
from gymnasium import spaces

class VNEEnv(gym.Env):
    """仮想ネットワーク埋め込み環境（簡易版）"""

    def __init__(self):
        super(VNEEnv, self).__init__()

        # 物理ノード数（例: 5ノード）
        self.num_nodes = 5

        # 状態空間: 各ノードの使用率（連続値: 0.0〜1.0）
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(self.num_nodes,), dtype=np.float32)

        # 行動空間: 仮想ノードをどの物理ノードにマッピングするか（整数: 0〜4）
        self.action_space = spaces.Discrete(self.num_nodes)

        # 内部状態（ノード使用率）
        self.node_usage = np.zeros(self.num_nodes, dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.node_usage = np.zeros(self.num_nodes, dtype=np.float32)
        observation = self.node_usage.copy()
        info = {}
        return observation, info

    def step(self, action):
        # まだダミー（ロジックは次のステップで実装）
        reward = 0.0
        done = False
        info = {}

        observation = self.node_usage.copy()
        return observation, reward, done, False, info

    def render(self):
        print(f"Node usage: {self.node_usage}")
