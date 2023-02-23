import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np
from os import path


class RAEnv(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30
    }

    def __init__(self, g=10.0):
        self.max_speed = 40
        self.max_torque = 15.
        self.dt = .05
        self.g = g
        self.m = 1.
        self.l = 1.
        self.viewer = None

        high = np.array([1., 1., self.max_speed, 1, 1], dtype=np.float32)
        self.action_space = spaces.Box(
            low=-self.max_torque,
            high=self.max_torque, shape=(1,),
            dtype=np.float32
        )
        self.observation_space = spaces.Box(
            low=-high,
            high=high,
            dtype=np.float32
        )
        self.seed()

        self._max_episode_steps = 200

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, u):
        th, thdot = self.state  # th := theta

        g = self.g
        m = self.m
        l = self.l
        dt = self.dt

        reward = 0
        self.steps += 1

        u = np.clip(u, -self.max_torque, self.max_torque)[0]
        self.last_u = u  # for rendering
        #costs = angle_normalize(th) ** 2 + .1 * thdot ** 2 + .001 * (u ** 2)

        newthdot = thdot + (-3 * g / (2 * l) * np.sin(th + np.pi) + 3. / (m * l ** 2) * u) * dt
        newth = th + newthdot * dt
        newthdot = np.clip(newthdot, -self.max_speed, self.max_speed)

        done = newth < -math.pi/2*1.2 \
               or newth > math.pi/2*1.2
        done = bool(done)

        if done:
            reward = -50 - (abs(newth)-math.pi/2)*50
            return self._get_obs(), reward, done, {}

        region1 = newth >= math.pi/4*0.8 and newth <= math.pi/4*1.2
        region2 = newth >= -math.pi/4*1.2 and newth <= -math.pi/4*0.8

        if region1:
            if not self.region1_crossed and self.region1_count <= 5:
                self.region1_count += 1
                reward = 10
            elif self.region1_count > 5:
                self.region1_crossed = True

        if region2 and self.region1_crossed:
            if not self.region2_crossed and self.region2_count <= 5:
                self.region2_count += 1
                reward = 10
                #print('done once')
            elif self.region2_count > 5:
                self.region2_crossed = True

        if self.region1_crossed and self.region2_crossed:
            # done = True
            self.region1_crossed = False
            self.region2_crossed = False
            self.region1_count = 0
            self.region2_count = 0

        if self.steps >= self._max_episode_steps:
            done = True
            return self._get_obs(), reward, done, {}

        self.state = np.array([newth, newthdot])
        return self._get_obs(), reward, done, {}

    def reset(self):
        high = np.array([np.pi, 1])
        self.state = self.np_random.uniform(low=-high, high=high)
        self.last_u = None
        self.region1_crossed = False
        self.region2_crossed = False
        self.region1_count = 0
        self.region2_count = 0
        self.steps = 0
        return self._get_obs()

    def _get_obs(self):
        theta, thetadot = self.state
        return np.array([np.cos(theta), np.sin(theta), thetadot, self.region1_crossed, self.region2_crossed])

    def render(self, mode='human'):
        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(500, 500)
            self.viewer.set_bounds(-2.2, 2.2, -2.2, 2.2)

            rod1 = rendering.make_capsule(1.3, .2)
            rod1.set_color(1, 1, 0.3)
            self.pole1 = rendering.Transform()
            rod1.add_attr(self.pole1)
            self.viewer.add_geom(rod1)
            self.pole1.set_rotation(-np.pi/4 + np.pi / 2)

            rod2 = rendering.make_capsule(1.3, .2)
            rod2.set_color(0.5,0.95,0.5)
            self.pole2 = rendering.Transform()
            rod2.add_attr(self.pole2)
            self.viewer.add_geom(rod2)
            self.pole2.set_rotation(np.pi / 4 + np.pi / 2)

            rod_safe1 = rendering.make_capsule(1.5, .1)
            rod_safe1.set_color(0.8, 0.0, 0.0)
            self.pole_safe1 = rendering.Transform()
            rod_safe1.add_attr(self.pole_safe1)
            self.viewer.add_geom(rod_safe1)
            self.pole_safe1.set_rotation(np.pi / 2 + np.pi / 2)

            rod_safe2 = rendering.make_capsule(1.5, .1)
            rod_safe2.set_color(0.8, 0.0, 0.0)
            self.pole_safe2 = rendering.Transform()
            rod_safe2.add_attr(self.pole_safe2)
            self.viewer.add_geom(rod_safe2)
            self.pole_safe2.set_rotation(-np.pi / 2 + np.pi / 2)

            rod = rendering.make_capsule(1, .2)
            rod.set_color(.8, .3, .3)
            self.pole_transform = rendering.Transform()
            rod.add_attr(self.pole_transform)
            self.viewer.add_geom(rod)

            axle = rendering.make_circle(.05)
            axle.set_color(0, 0, 0)
            self.viewer.add_geom(axle)
            fname = path.join(path.dirname(__file__), "assets/clockwise.png")
            self.img = rendering.Image(fname, 1., 1.)
            self.imgtrans = rendering.Transform()
            self.img.add_attr(self.imgtrans)

        self.viewer.add_onetime(self.img)
        self.pole_transform.set_rotation(self.state[0] + np.pi / 2)
        if self.last_u:
            self.imgtrans.scale = (-self.last_u / 2, np.abs(self.last_u) / 2)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None

def angle_normalize(x):
    return (((x+np.pi) % (2*np.pi)) - np.pi)

