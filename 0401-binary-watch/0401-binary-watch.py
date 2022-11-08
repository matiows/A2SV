class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        if turnedOn > 8:
            return []
        
        def changeTime(hour, minute):
            if minute < 10:
                str_min = '0' + str(minute)
            else:
                str_min = str(minute)
                
            return str(hour) + ':' + str_min
        
        def backtrack(index, hour, minute, count):
            if count == 0:
                answer.append(changeTime(hour, minute))
                return
            
            if index >= 10:
                return
            
            if index < 4:
                cur_hour = hour + 2 ** index
                if cur_hour < 12:
                    backtrack(index + 1, cur_hour, minute, count - 1)
                backtrack(index + 1, hour, minute, count)
            else:
                cur_min = minute + 2 ** (index - 4)
                if cur_min < 60:
                    backtrack(index + 1, hour, cur_min, count - 1)
                    
                backtrack(index + 1, hour, minute, count)
        backtrack(0, 0, 0, turnedOn)
        return answer
                