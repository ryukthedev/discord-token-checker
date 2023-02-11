import requests

from ui import UI

class Checker:

	def __init__(self) -> None:
		self.checked: bool = 0
		self.valid: bool = 0
		self.invalid: bool = 0

	def save_results(self, valid: list) -> None:

		with open("valid.txt", "a+") as f:
			f.write("\n".join(valid))

	def validate(self, token: str) -> bool:

		headers = {
			"Authorization": token
		}

		check = session.post("https://discord.com/api/v6/invite/valorant", headers=headers)

		if check.status_code == 400:
			return True
		else:
			return False

	def start(self) -> None:

		ui.clear()

		valid = []

		for token in tokens:
			validate = self.validate(token)
			self.checked += 1
			if validate:
				print(f"{ui.prefix} Valid: {ui.red}{token}{ui.reset}")
				self.valid += 1
				valid.append(token)
			else:
				self.invalid += 1

		print(f"{ui.prefix} Checked {ui.red}{self.checked:,}{ui.reset} tokens, {ui.red}{self.valid:,}{ui.reset} were good, {ui.red}{self.invalid:,}{ui.reset} were bad.")

		self.save_results(valid)

def load_tokens() -> list:

	with open("tokens.txt") as f:
		tokens = f.read().splitlines()

	return tokens

if __name__ == "__main__":

	tokens = load_tokens()
	session = requests.Session()

	ui = UI()
	checker = Checker()
	checker.start()
