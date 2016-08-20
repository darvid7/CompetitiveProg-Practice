#include <iostream>;
#include <string>;
#include <vector>;

using namespace std;

int main(){
    int T, N,t,i,j;
    cin >> T;

    for (t=1;t<=T;t++){
        cin>>N;
        cin.ignore();
        string curName, bestName;
        int curCount, bestCount;
        bestCount = 0;
        for (i=0;i<N;i++) {

            getline(cin, curName);
            curCount = 0;
            vector<bool> appeared(26, false);
            int asdf = (int)curName.length();
            for (j=0;j<asdf;j++){
                if (!appeared[curName[j]-'A']){
                    curCount++;
                    appeared[curName[j]-'A'] = true;
                }
            }

            if (curCount > bestCount){
                bestCount = curCount;
                bestName = curName;
            }
            else if ((curCount == bestCount) && (curName.compare(bestName) < 0)) {
                bestName = curName;
            }

        }

        cout << "Case #" << t << ": " << bestName << endl;
    }

    return 0;

}
