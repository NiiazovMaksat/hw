from random import randint

class ControlGame():
    def __init__(self, player_nums: dict):
        self.secret_nums = [6, 1, 2, 5]#self.create_secret_nums()
        self.player_nums = player_nums
        player_nums = self.parse_nums(self.player_nums)
        secret_nums = self.parse_nums(self.secret_nums)
        self.bulls = self.count_bulls(player_nums, secret_nums)
        self.cows = self.count_cows() - self.bulls

    def create_secret_nums(self):
        nums = []
        while len(nums) < 4:
            num = randint(1,10)
            if num not in nums:
                nums.append(num)
        return nums

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





d = [6, 1, 5, 2]
a = ControlGame(d)
a.print_nums()
print(a.bulls)



