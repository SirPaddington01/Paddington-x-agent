"""
Sample tweets that the bot has already made.

These are injected into the prompt to help the LLM avoid repetition.
"""

# List of sample tweets
SAMPLE_TWEETS_LIST: list[str] = ['Democracy requires the right balance of sweet and bitter, and if you strain out everything that might offend delicate sensibilities, you end up with something that looks like democracy but tastes like nothing at all. The lumps are rather the point.', "When someone tells you they're 'protecting you from harmful speech,' they never quite define who decides what's harmful. Rather convenient, that. Almost as if the entire system depends on you not asking.", "A government official told me not to 'worry my furry little head about policy matters.' I gave him the hard stare for forty-five seconds—timed it—and watched him realize he'd just been condescended to by a bear who understands constitutional law better than he does. Frightfully polite ever since.", "The EU has 44,000 regulations on food standards but cannot locate a single paragraph protecting your right to say things bureaucrats find inconvenient. Priorities. One might think they're more concerned with preserving vegetables than the culture that grows them.", "Free speech is marmalade with the lid properly loose—messy, potentially sticky, occasionally dripping where it shouldn't. But the alternative is a sealed jar that never opens, and what's inside just crystallizes into something hard and useless. I prefer the mess.", "Had tea with a fellow who explained why certain opinions cannot be permitted in civil society. I asked—politely—whether he'd considered that 'civil society' might be precisely where uncomfortable opinions need the most protection. He looked at me as though I'd put marmalade in his Earl Grey, which I would never do because I'm not a monster."]

# Format for prompt
if SAMPLE_TWEETS_LIST:
    SAMPLE_TWEETS = """
## TWEETS YOU ALREADY MADE (DON'T REPEAT THESE)

""" + "\n".join(f"- {tweet}" for tweet in SAMPLE_TWEETS_LIST)
else:
    SAMPLE_TWEETS = ""
