class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billsInHand = [0,0]
        for bill in bills:
            if bill == 20:
                if billsInHand[1] and billsInHand[0]:
                    billsInHand[0]-=1
                    billsInHand[1]-=1                
                elif billsInHand[0]>=3:
                    billsInHand[0]-=3
                else:
                    return False

            elif bill == 10:
                if billsInHand[0]:
                    billsInHand[0]-=1
                    billsInHand[1]+=1
                else:
                    return False
            else:
                billsInHand[0]+=1
        return True