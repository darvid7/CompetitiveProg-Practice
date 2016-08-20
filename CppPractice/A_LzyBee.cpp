#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T, variations;

	cin >> T;

	for (int i=0; i<T; i++){
		string s;
		cin >> s;
        cout << "Case #" << i+1 << ": ";
		if (s.length() <= 1){
			cout << 1 <<endl;
		} else {
			variations = 1;
			for (int j=0; j<s.length(); j++){
				int dif = 0;

				if ( (j > 0) && (j < s.length()-1) ){
					if (s[j-1] != s[j]){
						dif += 1;
					}
					if (s[j+1] != s[j]){
						dif += 1;
					}

				} else if (j == 0){
					if (s[j+1] != s[j]){
						dif += 1;
					}
				} else if (j == s.length()-1){
					if (s[j-1] != s[j]){
						dif += 1;
					}
				}

				dif += 1;

				variations = variations * dif;
			}

			cout << variations << endl;
		}
	}


	return 0;
}
