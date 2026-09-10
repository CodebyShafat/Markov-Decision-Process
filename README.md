# 🧠 Markov Decision Process (MDP)

> A beginner-friendly implementation of a **Markov Decision Process (MDP)** using the **Value Iteration** algorithm in pure Python.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-Value%20Iteration-8A2BE2?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</p>

---

## 📌 About

This project implements a simple **Markov Decision Process** in Python using a Weather & Commute scenario. The program represents different weather conditions as states, allows the agent to choose between walking and taking the bus, assigns rewards to each decision, models the probability of weather changes, and uses **Value Iteration** to calculate the long-term value of each state and determine the optimal policy.

The implementation is intentionally kept simple and uses only standard Python features, making it easy to understand, run, and explain.

---

## 🎯 Problem Statement

Imagine an agent that needs to travel depending on the current weather. On a sunny day, walking is more rewarding than taking the bus, while on a rainy day, taking the bus is a better choice. However, the weather can change in the future, so the agent must consider both the immediate reward and the expected future rewards before selecting an action.

The goal is to find the **optimal policy** that maximizes the expected long-term reward.

---

## 🧩 MDP Components

A Markov Decision Process is represented using four main components: **States, Actions, Rewards, and Transition Probabilities**. This implementation also uses a discount factor to control the importance of future rewards.

| Component | Description |
|---|---|
| **States** | `Sunny`, `Rainy` |
| **Actions** | `Walk`, `Bus` |
| **Rewards** | Reward received for each state-action pair |
| **Transitions** | Probability of moving to the next weather state |
| **Discount Factor** | `γ = 0.9` |

---

## 🌦️ Environment

The environment contains two possible states:

```text
☀️ Sunny
🌧️ Rainy