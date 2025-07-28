def build_prompt(persona, task, content):
    return (
        f"Act as a professional assistant for a {persona} whose task is: {task}.\n\n"
        f"Document section:\n{content}\n\n"
        f"Answer:\n1. Is this relevant?\n2. If yes, give a 2-line summary."
    )
