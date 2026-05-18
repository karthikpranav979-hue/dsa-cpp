class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n==1){
            return true;
        }
        if(n>0 and n%4==0){
            return isPowerOfFour(n/4);   // n/2 for power 2 & 3 ...
        }
        else{
            return false;
        }
    }  
