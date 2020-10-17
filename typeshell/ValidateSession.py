import argparse
from typeshell.testmanager.TestManager import TestManager

class ValidateSession(argparse.Action):
	def __call__(self, parser, args, values, option_string=None):
		prompt_count = int(values[0])
		prompt_type = values[1]
		valid_prompt_types = list(TestManager().prompts.keys())
		if prompt_type not in valid_prompt_types:
			raise(ValueError(f"Invalid prompt types. Did you mean: {', '.join(valid_prompt_types)}"))
		setattr(args, self.dest, (prompt_count, prompt_type))