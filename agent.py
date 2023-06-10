import openai

# Set up the OpenAI API client
openai.api_key = "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"

class Agent:
    def __init__(self, model="text-davinci-003", temp=0.5, goal_state=(0,0)):
        self.model = model
        self.temp = temp
        self.goal_state = goal_state
        self.previous_states = []

    def generate_prompt(self, state, remind=False):
        return f"""Your goal is to make your position as close to {self.goal_state} as possible. Moving left decreases the 
               first coordinate, while moving right increases the first coordinate. Moving up decreases the second coordinate,
               while moving down decreases the second coordinate. Saying 'noop' keeps you in the same place. Your current 
               position is {state}. In order to get closer to {self.goal_state}, will you go up, left, right, down, or noop?""" # Reminding of the goal at the end of the prompt makes it work

    def policy(self, state):
        prompt = self.generate_prompt(state)
        completion = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=self.temp,
        )
        response = completion.choices[0].text
        return response

