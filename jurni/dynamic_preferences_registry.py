from dynamic_preferences.types import StringPreference
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.preferences import Section

DEFAULT_PROMPT = """\
You're the narrator of a bedtime story, reading to a child of {age} years old.
The child's name is {name}. The child's favorite color is {favorite_color}.
The child is a {gender}.
"""


general = Section('general')

@global_preferences_registry.register
class InitialPrompt(StringPreference):
    name = 'initial_prompt'
    default = DEFAULT_PROMPT