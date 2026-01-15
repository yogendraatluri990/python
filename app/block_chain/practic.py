# def anagram_user(strs: list[str]):
#      list_mapper: dict[str, list[str]] = {}
#      if len(strs) <= 0:
#             return []
#      for word in strs:
#             #split the word into characters and sort them
#             sort_word = "".join(sorted(word))
#             if sort_word not in list_mapper:
#                 list_mapper[sort_word] = [word] 
#             else:
#                 list_mapper[sort_word].append(word)
            
#      return list(list_mapper.values())

# print(anagram_user(["act","pots","tops","cat","stop","hat"]))

# sample_tuple:tuple[int, str, float] = (1, "yogendra", 99.9)

# index, name, score = sample_tuple
# print(f"Index is {index}, Name is {name}, Score is {score}")

def topKFrequency(nums: list[int], k:int) -> list[int]:
    frequency:dict[int, list[int]] = {}
    r = []
    if len(nums) <= 0:
        return []
    
    for num in nums:
        if num not in frequency:
            frequency[num] = [num]
        else:
            frequency[num].append(num)
    for f in sorted(frequency.keys(), key=lambda x: len(frequency[x]), reverse=True):
        if len(r) < k:
            r.append(f)
    
    return r

print(topKFrequency([1,2,2,3,3,3],2))


def construct_dict(ranDic: dict[str, int]) -> list[str]:
     if len(ranDic) <= 0:
         return []
      #sDict = dict(sorted(ranDic.keys(), key=lambda x: len(ranDic[x]), reverse=True))
     return [k for k in ranDic.keys()]