class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # base case
        if N == 1 or not dislikes:
            return True
            
        # dfs approach to find if two perons in dislike group don't share same color
        def dfs( people, color ):
            color_list[people] = color            
            for next_person in graph[ people ]:
                if color_list[next_person] == color:
                    return False
                if color_list[next_person] == 0 and (not dfs( next_person, -color)):
                    return False      
            return True
        
        
        graph = collections.defaultdict( list )
        color_list = [ 0 for _ in range(N+1) ]
        for a, b in dislikes:
            graph[a].append( b )
            graph[b].append( a )            
        
        for people in range(1, N+1):
            if color_list[people] == 0 and (not dfs( people,1)):
                return False 
        return True
