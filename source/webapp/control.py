from random import randint
secret = []
history = []
class ControlGame():
    def __init__(self, player_nums: dict):
        self.secret_nums = secret
        self.create_secret_nums()
        self.player_nums = player_nums

        player_nums = self.parse_nums(self.player_nums)
        secret_nums = self.parse_nums(self.secret_nums)
        self.bulls = self.count_bulls(player_nums, secret_nums)
        self.cows = self.count_cows() - self.bulls
        global history
        history.append(player_nums)
        self.history = history

    def add_player_nums(self, player_nums: dict):
        self.player_nums = player_nums

    def create_secret_nums(self):
        global secret
        if len(secret)<1:
            while len(secret) < 4:
                num = randint(1,10)
                if num not in secret:
                    secret.append(num)

    def count_bulls(self, player_nums, secret_nums):
        bulls = 0
        i = 1
        while i < 5:
            if player_nums[i] == secret_nums[i]:
                bulls += 1
            i += 1
        return bulls

    def count_cows(self):
        cows = 0
        i = 0
        while i < 4:
            if self.player_nums[i] in self.secret_nums:
                cows += 1
            i += 1
        return cows

    def parse_nums(self, nums):
        parsed = {
            1: nums[0],
            2: nums[1],
            3: nums[2],
            4: nums[3]
        }
        return parsed
