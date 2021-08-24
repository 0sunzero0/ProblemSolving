class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()
        
        '''
        sorting
        def fn(s):
            return s[0],s[1]
        sorted(c, key=fn)
        '''
