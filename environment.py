from models import Observation, Action
from tasks import tasks

class CustomerEnv:

    def __init__(self):
        self.ticket = ""
        self.done = False
        self.current_task = None
        self.steps = 0
        self.last_action = None

    def reset(self, task_type="easy"):
        self.current_task = tasks[task_type]
        self.ticket = self.current_task["ticket"]
        self.done = False
        self.steps = 0
        self.last_action = None
        return Observation(ticket=self.ticket, status="open")

    def calculate_reward(self, action: Action):
        reward = 0.0
        expected = self.current_task["expected"]

        self.steps += 1

        # Reward correct keyword
        if expected in action.message.lower():
            reward += 0.3

        # Encourage correct sequence
        if self.last_action is None and action.action_type == "classify":
            reward += 0.2

        elif self.last_action == "classify" and action.action_type == "reply":
            reward += 0.4

        elif self.last_action == "reply" and action.action_type == "close":
            reward += 0.6
            self.done = True

        # Penalize repeating same action
        if action.action_type == self.last_action:
            reward -= 0.3

        # Penalize long loops
        if self.steps > 4:
            reward -= 0.1

        self.last_action = action.action_type

        return max(reward, 0.0)

    def step(self, action: Action):
        reward = self.calculate_reward(action)
        return Observation(ticket=self.ticket, status="closed"), reward, self.done, {}

    def state(self):
        return {"ticket": self.ticket}