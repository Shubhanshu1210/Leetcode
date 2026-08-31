class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<int> arow(m, 1);
        vector<int> acol(n, 1);      
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(matrix[i][j]==0){
                    arow[j]=0;
                    acol[i]=0;
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(matrix[i][j]!=0){
                    if(arow[j]==0 || acol[i]==0){
                        matrix[i][j]=0;
                    }
                }
            }
        }
    }
    
    
};