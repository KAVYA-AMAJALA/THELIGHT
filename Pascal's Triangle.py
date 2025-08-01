class Solution:
    def generate_row(self,row:int)->list[int]:
        ans_row=[1]
        ans=1
        for col in range(1,row):
            ans=ans*(row-col)//col
            ans_row.append(ans)
        return ans_row
    def generate(self, numRows: int) -> List[List[int]]:
        final_ans=[]
        for i in range(1,numRows+1):
            ans_row=self.generate_row(i)
            final_ans.append(ans_row)
        return final_ans
       
