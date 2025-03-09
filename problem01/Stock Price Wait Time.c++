#include <iostream>
#include <vector>
#include <stack>
#include <sstream>
using namespace std;

void stock_days(vector<int> arr){
    // create a stack that holds indexes
    stack<int> stk;
    vector <int> res;
    for (int i = 0; i < arr.size(); i++){
        res.push_back(0);
    }
    //int j = 0;
    for (int j = 0; j < arr.size(); j++){
        while ((stk.size() != 0) && (arr[j] > arr[stk.top()])){
            // get the previous index 
            int prv_index = stk.top();
            stk.pop();
            res[prv_index] = j - prv_index;

        }
        stk.push(j);
    
    }
    for (int n: res){
        cout << n << " ";
    }


}


int main(){
    int n;
    cin >> n;
    cin.ignore();
    vector<int> arr;
    string str;
    getline(cin, str);
    stringstream ss(str);
    int num;
    
    while (ss >> num){
        arr.push_back(num);
    }
    
    stock_days(arr);
    return 0;

}