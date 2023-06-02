# 响应封装

import json
from typing import List


class res_api:
    def __init__(self, **params) -> None:
        print(params)
        pass


def tosum(nums: List[int], target: int):
    print(f"nums,tagfet:{nums,target}")
    d = dict()
    for i, num in enumerate(nums):
        print(f"i,num:{i,num}")
        if target-num in d:
            return [d[target - num], i]
        d[nums[i]] = i
        print(f"d:{d}")


def isPalindrome(s: str) -> bool:
    if len(s) == 0:
        return True
    s = list(filter(str.isalnum, list(s)))
    print(f"s:{s}")

    stra = 0
    end = len(s)-1
    while stra < end:
        # while s[stra] is None or s[stra].isalnum() != True:
        #     if stra < len(s)-1:
        #         stra += 1
        #     else:
        #         return False
        # while s[end] is None or s[end].isalnum() != True:
        #     if end > 1:
        #         end -= 1
        #     else:
        #         return False
        if s[stra].lower() != s[end].lower():
            return False
        stra += 1
        end -= 1

    return True


def lengthOfLongestSubstring(s: str) -> int:
    maxlen = 0
    p1=0
    p2=0
    while p2<len(s):
        print(f"s[p2]:{s[p2]}")
        print(f"find:{s.find(s[p2],p1,p2)}")
        if not s.find(s[p2],p1,p2)==-1:
            print(f"p2:{p2}")
            if maxlen<p2-p1:
                maxlen=p2-p1+1
            
        else:
            p1+=1
            p2-=1
        p2+=1


    return maxlen


if __name__ == "__main__":
    # 两数之和
    # print(123)
    # nums = [2, 7, 11, 15]
    # target = 9
    # print("result",tosum(nums,target))

    # 回文
    # s = "a."
    # print(isPalindrome(s))

    # 最长不重复子串
    s = "aa"
    print(lengthOfLongestSubstring(s))
