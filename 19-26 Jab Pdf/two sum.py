def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        answer = []

        n = len(nums)
        for i in range(n):
            otherele = target - nums[i]
            if(otherele in hash_map):
                answer.append(hash_map[otherele])
                answer.append(i)
            else:
                hash_map[nums[i]] = i
        
        return answer
