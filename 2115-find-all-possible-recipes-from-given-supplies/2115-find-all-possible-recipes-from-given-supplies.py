class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        incoming = defaultdict(int)
        relation = defaultdict(list)
        start = set()
        supply = set(supplies)
        check = set(recipes)
        dish = []
        
        for recipe, ingredient in zip(recipes, ingredients):
            for item in ingredient:
                if item in supplies:
                    start.add(item)
                
                relation[item].append(recipe)
                incoming[recipe] += 1
                
        queue = deque(start)
        
        while queue:
            item = queue.popleft()
            if item in check:
                dish.append(item)
                
            for sub in relation[item]:
                if sub in incoming:
                    incoming[sub] -= 1
                    if incoming[sub] == 0:
                        queue.append(sub)
                        
        return dish
                
            
                