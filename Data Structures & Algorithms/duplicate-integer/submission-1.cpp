class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool dup = false;
        if(nums.empty()) {
            return dup;
        }
        for(int i = 0; i < nums.size(); i++) {
            for(int j = i +1; j < nums.size(); j++) {
                if(nums[i] == nums[j]) {
                    dup = true;
                    return dup;
                }
            }
        }
        return dup;
    }
};