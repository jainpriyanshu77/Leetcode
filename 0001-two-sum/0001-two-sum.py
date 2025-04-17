class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # ek khaali hash map banaya jisme number aur uski index store hogi
        for i, num in enumerate(nums):  # array ke har element ke saath uski index bhi le rahe hain
            compl = target - num  # hume target banane ke liye jo number chahiye, uska complement nikala
            if compl in num_map:  # agar wo complement pehle se map me maujood hai
                return [num_map[compl], i]  # dono index return kar do jinka sum target ban raha hai
            num_map[num] = i  # agar nahi mila, to current number ko map me daal do future ke use ke liye

