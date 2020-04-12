#include <iostream>
using namespace std;

int main(){
	int n, radius;
	cin >> n >> radius;
	
	int arr[n];
	for (int i = 0; i < n; ++i) cin >> arr[i];
	
	int ans = 0, heated0ToN = -1;
	while (heated0ToN < n - 1) {
		int pos = -1;
		
		for (int i = n - 1; i > max(-1, heated0ToN - radius + 1); --i) {
			if (arr[i] == 1 && i - radius <= heated0ToN) {
				pos = i;
				break;
			}
		}
		
		if (pos == -1) { ans = -1; break; }
		
		ans++;
		heated0ToN = pos + radius - 1;
	}
	cout << ans << "\n";
}