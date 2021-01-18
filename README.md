# Modular_Deep_RL_E-LDGBA

The repository implements a modular Deep Deterministic Policy Gradients (DDPG) Reinforcement Learning (RL) with liear temporal logic specifications as high-level misstion specifications. 

[Project Webpage](https://github.com/mingyucai/Modular_Deep_RL/)

<br>

## The Environment
The task is performed on a custom environment developed using Gym-OpenAI from [DeepRL-LTL](https://github.com/RickyMexx/DeepRL-LTL). The 6-dimensional state consists of the position and velocity along the x and y axes and two binary values (one for each circle) specifying whether the agent has gone through a circle. There are two circles in a specified order: bottom-left, top-right and a ball as the agent.

![Ball-Pass](/Images/Ball-Pass_environment.jpg)

<br>

## Results

### Task 2



<br>

### Task 2
The task 2 is required to visit region 1, and then region 2. Here we compare the mean and standard deviation of rewards during training for two method: (i) modular DDPG + E-LDGBA; (ii) standard DDPG + E-LEGBA.

<br><br>

Standard DDPG fails to reach the two balls with high success rate.  The modular DDPG (on the right), instead, is able to completely solve the specified task with 100% success rate.


![Standard](https://github.com/mingyucai/Modular_Deep_RL_E-LDGBA/blob/main/Images/Standard_DDPG_2.gif) ![Modular](/Images/Modular_DDPG_2.gif)


<br>
