class Solution {
public:
    vector<int> generaterow(int row){
        long long ans = 1;
        vector<int> ansroww;
        ansroww.push_back(ans);
        for(int col=1;col<row;col++){
            ans = ans*(row-col);
            ans = ans/col;
            ansroww.push_back(ans);
        }
        return ansroww;
    }
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for(int i=1; i<=numRows;i++){
            ans.push_back(generaterow(i));
        }
        return ans;
    }
};