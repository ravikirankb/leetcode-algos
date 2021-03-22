class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in items:
            if ruleKey == 'type' and i[0] == ruleValue:
                count += 1
            elif ruleKey == 'color' and i[1] == ruleValue:
                count += 1
            elif ruleKey == 'name' and i[2] == ruleValue:
                count += 1
        return count
