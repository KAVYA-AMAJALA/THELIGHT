class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
         int size = nums.size();
        vector<int> suffixArray(size);
        for(int indx = size - 1; indx > -1; indx--){
            if(indx == size - 1)suffixArray[indx] = nums[indx];
            else suffixArray[indx] = nums[indx] * suffixArray[indx + 1];
        }
        int prefixProduct = 1;
        for(int indx = 0; indx < size; indx++){
            int updatedValue = prefixProduct * ((indx + 1 < size) ? suffixArray[indx+1] : 1);
            suffixArray[indx] = updatedValue;
            prefixProduct *= nums[indx];
        }
        return suffixArray;
    
    }
};
