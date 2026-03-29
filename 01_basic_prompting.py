from rich.console import Console
from rich.panel import Panel

from workshop_client import ask_llm, DEFAULT_MODEL

console = Console()

messages = [
    {
        "role": "system",
        "content": "You are a concise teaching assistant for beginners learning AI.",
    },
    {
        "role": "user",
        # "content": "Explain AI like I'm 10 years old.",
        # "content": "Explain AI in exactly 1 sentence.",
        # "content": "Explain AI as if you're a rapper.",
        "content": "Explain AI with one bullet point, dont use jargons,explain in simple english, try to flow the constraint.",
    },
]

answer = ask_llm(messages, model=DEFAULT_MODEL)

console.print(Panel.fit(answer, title=f"Model response ({DEFAULT_MODEL})"))
