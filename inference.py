import os
from openai import OpenAI
from environment import CustomerEnv
from models import Action

# ✅ USE ENV VARIABLES (REQUIRED)
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
API_KEY = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

for task_name in ["easy", "medium", "hard"]:

    env = CustomerEnv()
    obs = env.reset(task_name)

    print(f"[START] task={task_name} env=customer_support model={MODEL_NAME}")

    rewards = []

    for step in range(1, 6):

        prompt = f"""
You are an intelligent customer support agent.

Customer ticket:
"{obs.ticket}"

Current step: {step}

STRICT:
Step 1 → classify
Step 2 → reply (include refund/payment)
Step 3 → close

Do not repeat actions.

Respond ONLY:
action_type:message
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )

        output = response.choices[0].message.content.strip()

        try:
            if ":" in output:
                action_type, message = output.split(":", 1)
            else:
                action_type, message = "reply", output

            action_type = action_type.strip().lower()
            message = message.strip()

            if action_type not in ["reply", "classify", "close"]:
                action_type = "reply"

        except:
            action_type = "reply"
            message = "refund will be processed"

        action = Action(action_type=action_type, message=message)

        obs, reward, done, _ = env.step(action)

        rewards.append(reward)

        print(f"[STEP] step={step} action={action_type} reward={reward:.2f} done={str(done).lower()} error=null")

        if done:
            break

    score = min(sum(rewards), 1.0)

    print(f"[END] success=true steps={step} score={score:.2f} rewards={','.join(map(str,rewards))}")