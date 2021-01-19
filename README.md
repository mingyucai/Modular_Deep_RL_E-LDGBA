# Modular_Deep_RL_E-LDGBA

The repository implements a modular Deep Deterministic Policy Gradients (DDPG) Reinforcement Learning (RL) with liear temporal logic specifications as high-level misstion specifications. 

[Project Webpage](https://github.com/mingyucai/Modular_Deep_RL/)

<br>

## The Environment
The task is performed on a custom environment developed using Gym-OpenAI from [DeepRL-LTL](https://github.com/RickyMexx/DeepRL-LTL). 
<img src="https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/Ball-Pass_environment.jpg" width="400" height="300">
<br>

## Results

### Task 1
The task 1 is a surveillance mission that requireds to s visit region 1 and region 2 periodically (infinite horizon). The modular DDPG (on the left) is able to completely solve the specified task with 100% success rate. Standard DDPG (one the right) fails for this repetitve pattern. 

![Modular](/Images/Task1_modular.gif)
![Standard](/Images/Task1_standard.gif)


<br><br>




<br>

### Task 2
The task 2 is required to visit region 1, and then region 2 (finite horizon). The modular DDPG (on the left) is able to completely solve the specified task with 100% success rate. The success rate of Standard DDPG (one the right) is around 86%. 

![Modular](/Images/Tas2_modular.gif)
![Standard](/Images/Task2_standard.gif)


<br><br>

Here we compare the mean and standard deviation of rewards during training for two method: (i) modular DDPG + E-LDGBA; (ii) standard DDPG + E-LEGBA.

![Rward](/Images/Task2_reward.jpg)


<br>
