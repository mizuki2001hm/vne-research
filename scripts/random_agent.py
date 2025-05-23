# scripts/random_agent.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.env.vne_env import VNEEnv

def run_random_agent(episodes=10):
    env = VNEEnv()
    total_rewards = []

    for ep in range(episodes):
        obs, info = env.reset()
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)

        total_rewards.append(reward)
        print(f"[Episode {ep+1}] Action: {action}, Reward: {reward}, Assigned: {info['assigned']}")

    avg_reward = sum(total_rewards) / len(total_rewards)
    print(f"\n✅ 平均報酬（{episodes}エピソード）: {avg_reward:.2f}")

    env.render()

if __name__ == "__main__":
    run_random_agent()