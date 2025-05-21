#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
from typing import List


# @lc code=start
class Solution:

    def candy(self, ratings: List[int]) -> int:

        def assign_candy(ratings):
            n = len(ratings)

            # base case
            if n <= 1:
                return n

            # special case: first two ratings are identical
            if ratings[0] == ratings[1]:
                return 1 + self.candy(ratings[1:])

            candies = [0]
            min_candies = 0
            recursive_ans = 0

            def update_min():
                nonlocal min_candies, candies
                if candies[-1] == min(candies):
                    min_candies = min(candies) - 1

            for i in range(1, n):
                pre_rating = ratings[i - 1]
                cur_rating = ratings[i]

                # special case: last child, no successive constraints
                if i == n - 1:
                    if pre_rating > cur_rating:
                        # greedy
                        update_min()
                        candies.append(min_candies)
                    else:
                        candies.append(candies[-1] + 1)
                    break

                next_rating = ratings[i + 1]

                # special case: adjacent identical ratings, recursively process rest part
                if cur_rating == next_rating:
                    if pre_rating > cur_rating:
                        # greedy
                        update_min()
                        candies.append(min_candies)
                    else:
                        candies.append(candies[-1] + 1)
                    recursive_ans = self.candy(ratings[i + 1:])
                    break

                # only remains strictly > or <
                # 0 1 2
                if pre_rating < cur_rating < next_rating:
                    candies.append(candies[-1] + 1)
                # 0 1 0
                elif pre_rating < cur_rating > next_rating:
                    candies.append(candies[-1] + 1)
                # 1 0 1
                elif pre_rating > cur_rating < next_rating:
                    # greedy
                    update_min()
                    candies.append(min_candies)
                # 2 1 0
                else:
                    candies.append(candies[-1] - 1)

            # at least 1 candy for everyone
            filler = 1 - min_candies
            candies = list(map(lambda x: x + filler, candies))

            return sum(candies) + recursive_ans

        return min(assign_candy(ratings[:]), assign_candy(ratings[::-1]))


# @lc code=end
print(Solution().candy([1, 2, 87, 87, 87, 2, 1]))
