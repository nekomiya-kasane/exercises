# Include your imports here, if any are used.

student_name = "Type your full name here."

# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        self.m_game = game
        self.m_discount = discount
        self.m_values = {} 

    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        if state in self.m_values:
            return self.m_values[state]
        return 0.

    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """
        t = self.m_game.get_transitions(state, action)
        
        sm = 0
        for _s, _p in t.items(): # state, probability
            rd = self.m_game.get_reward(state, action, _s)
            val = self.m_discount * self.get_value(_s)
            sm += _p * (rd + val)

        return sm

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        mx_arg = None
        mx_val = -float("inf")

        # iter all actions
        for _a in self.m_game.get_actions(state):
            val = self.get_q_value(state, _a)
            if val > mx_val:
                mx_arg = _a
                mx_val = val

        return mx_arg

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        
        values = {}

        for _s in self.m_game.states:
            actions = self.m_game.get_actions(_s)
            pool = [self.get_q_value(_s, a) for a in actions]
            if not len(pool):
                values[_s] = 0.0
            else:
                values[_s] = max(pool)
        
        # swap 
        self.m_values = values


# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function or
    override ValueIterationAgent's methods, you can add them as well.
    """

    def __init__(self, game, discount, epsilon=1e-6):
        super().__init__(game, discount)
        self.m_epsilon = epsilon

    def set_tolerance(self, epsilon):
        self.m_epsilon = epsilon

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until |V_{k+1}(s) - V_k(s)| < ε
        """
        
        policy = {}
        for _s in self.m_game.states:
            policy[_s] = self.get_best_policy(_s)

        while True:
            mx = 0.

            for _s in self.m_game.states:
                old = self.get_value(_s)
                new = self.get_q_value(_s, policy[_s])

                self.m_values[_s] = new # update

                mx = max(mx, abs(new - old))
            
            if mx < self.m_epsilon:
                break

# 3. Bridge Crossing Analysis
def question_3():
    discount = 0.9
    noise = 0.01
    return discount, noise

# 4. Policies
def question_4a():
    discount = 0.3
    noise = 0.01
    living_reward = -1
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = 0.5
    noise = 0.1
    living_reward = -1
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = 0.6
    noise = 0
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = 0.9
    noise = 0.1
    living_reward = 0.5
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = 0.1
    noise = 0
    living_reward = 10
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

# 5. Feedback
# Just an approximation is fine.
feedback_question_1 = 2.5

feedback_question_2 = """
It's a little hard for me to comprehend the model and policy 
choosing logics.
But after got the main idea, it seems interesting.
"""

feedback_question_3 = """
The assignment is well organized, and the structure and info-
mation is adequate and absorbing. It leads me to understand 
the whole idea step by step.
"""
