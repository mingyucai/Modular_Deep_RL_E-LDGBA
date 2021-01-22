# Modular_Deep_RL_E-LDGBA

The repository implements a modular Deep Deterministic Policy Gradients (DDPG) Reinforcement Learning (RL) with liear temporal logic specifications as high-level misstion specifications.  The project is based on a modified Soft-Actor-Critic algorithm based on the Py-Torch implementation provided at [Py-Torch SAC](https://github.com/pranz24/pytorch-soft-actor-critic) and 
The project applies a smodified Soft-Actor-Critic algorithm based on the Py-Torch implementation and a modular deep RL algorithm provided at [Py-Torch SAC](https://github.com/pranz24/pytorch-soft-actor-critic) and [DeepRL-LTL](https://github.com/RickyMexx/DeepRL-LTL).

[Project Webpage](https://github.com/mingyucai/Modular_Deep_RL/)

<br>

## Ball-Pass and Cart-Pole Environment
The task is performed on a custom environment developed using Gym-OpenAI from [DeepRL-LTL](https://github.com/RickyMexx/DeepRL-LTL) and [CartPole](https://gym.openai.com/envs/CartPole-v0/). 
<img src="https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/Ball-Pass%20and%20CartPole_environment.jpg" width="800" height="400" >
<br>

## Results for CartPole

Except preventing the CarPole from falling over, the task1 is a surveillance mission that requireds to s visit  region yellow and region green periodically (infinite horizon). The task2 requires to visit yellow first and then green (finite horizon). The deoms for task1 and task2 are shown in left and right respectively.



![task1](/Images/Task1_CartPole.gif)
![task2](/Images/Task2_CartPole.gif)


<br><br>

Here we compare the mean reward during training for task1 (left) and task2(right) with two method: (i) modular DDPG + E-LDGBA; (ii) standard DDPG + E-LEGBA.

<img src="https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/task_CartPole.jpg" width="600" height="200" >



<br>



## Results for Ball-Pass

### Task 1
The task 1 is a surveillance mission that requireds to s visit region 1 and region 2 periodically (infinite horizon). The modular DDPG (on the left) is able to completely solve the specified task with 100% success rate. Standard DDPG (one the right) fails for this repetitve pattern. 

![Modular](/Images/Task1_modular.gif)
![Standard](/Images/Task1_standard.gif)


<br><br>
Here we compare the mean and total reward during training for task1 with two method: (i) modular DDPG + E-LDGBA; (ii) standard DDPG + E-LEGBA.

<img src="https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/Task1_reward_.jpg" width="600" height="200" >




<br>

### Task 2
The task 2 is required to visit region 1, and then region 2 (finite horizon). The modular DDPG (on the left) is able to completely solve the specified task with 100% success rate. The success rate of Standard DDPG (one the right) is around 86%. 

![Modular](/Images/Tas2_modular.gif)
![Standard](/Images/Task2_standard.gif)


<br><br>
Here we compare the mean and total reward during training for task 2 with two method: (i) modular DDPG + E-LDGBA; (ii) standard DDPG + E-LEGBA.

<img src="https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/Task2_reward.jpg" width="600" height="200" >




<br>
