class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        
        best_root_idx = 0
        min_root_len = len(wordsContainer[0])
        
        for i, word in enumerate(wordsContainer):
            if len(word) < min_root_len:
                min_root_len = len(word)
                best_root_idx = i
                
        trie["best_idx"] = best_root_idx
        
        for i, word in enumerate(wordsContainer):
            curr_len = len(word)
            node = trie
            
            for char in reversed(word):
                if char not in node:
                    node[char] = {"best_idx": i}
                else:
                    best_i = node[char]["best_idx"]
                    if curr_len < len(wordsContainer[best_i]):
                        node[char]["best_idx"] = i
                node = node[char]
                
        ans = []
        for query in wordsQuery:
            node = trie
            last_valid_idx = trie["best_idx"]
            
            for char in reversed(query):
                if char in node:
                    node = node[char]
                    last_valid_idx = node["best_idx"]
                else:
                    break
            ans.append(last_valid_idx)
            
        return ans