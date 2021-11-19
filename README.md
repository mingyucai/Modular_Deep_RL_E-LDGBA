# Modular_Deep_RL_E-LDGBA

The repository implements a modular Deep Deterministic Policy Gradients (DDPG) Reinforcement Learning (RL) with liear temporal logic specifications as high-level misstion specifications. 

<br>

## Publications
* Mingyu Cai, Mohammadhosein Hasanbeig, Shaoping Xiao, Alessandro Abate, and Zhen Kan. "Modular deep reinforcement learning for continuous motion planning with temporal logic", IEEE Robotics and Automation Letters 6 (4), 7973-7980. [[PDF]](https://arxiv.org/pdf/2102.12855.pdf)

<br>

## Ball-Pass and Cart-Pole Environment
The tasks are performed on a custom environments in [DeepRL-LTL](https://github.com/RickyMexx/DeepRL-LTL) and [CartPole](https://gym.openai.com/envs/CartPole-v0/) developed via Gym-OpenAI
<img src="https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/Ball-Pass%20and%20CartPole_environment.jpg" width="800" height="400" >
<br>

## Results for CartPole using EP-MDP
In addition to preventing the Cartpole from falling over, Task1 is a surveillance mission that requires the cart to visit  region yellow and region green periodically (infinite horizon). Task2 requires the cart to visit yellow first and then green (finite horizon). The demos for Task1 and Task2 are shown in left and right respectively.

![task1](/Images/Task1_CartPole.gif)
![task2](/Images/Task2_CartPole.gif)

<br><br>

<br>

## Results for Ball-Pass using EP-MDP

### Task 1
Task1 is a surveillance mission that requires the ball to visit region 1 and region 2 periodically (infinite horizon). The modular DDPG (on the left) can completely solve the specified task with a 100% success rate. Standard DDPG on the right (the worst scenarios) fails for this repetitve pattern. 

![Modular](/Images/Task1_modular.gif)
![Standard](/Images/Task1_standard.gif)

<br><br>

<br>

### Task 2
Task2 requires the ball to visit region 1, and then region 2 (finite horizon). The modular DDPG (on the left) is able to completely solve the specified task with a 100% success rate. The success rate of Standard DDPG (on the right) is around 86%. 

![Modular](/Images/Tas2_modular.gif)
![Standard](/Images/Task2_standard.gif)

<br><br>

<br>

## Comparison with Standard Product MDP
Here are the results (the worst scenarios) using Standard Product MDP, which cannot guarantee the completion of repetitive tasks over the infinite horizon in the CartPole and Ball-Pass problems, respectively.


![CartPole](/Images/CartPole_P-MDP.gif)
![Bass-pass](/Images/Ball-pass_P-MDP.gif)

<br><br>

<br>
