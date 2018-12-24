#include <iostream>
#include <vector>

using namespace std;

void func(vector<int> v)
{
	int i = 0;
	int arr2[v.size()];
		
	for (int r = 0; r < v.size(); r++)
	{
		if (v[r] != 0)
		{
			arr2[i] = v[r];
			i++;
		}	
	}
	
	for (int k = i; k < v.size(); k++)
	{
		arr2[k] = 0;
	}	
		
	for (int x = 0; x < v.size(); x++)
	{
	    cout << arr2[x] << endl;
	}
    
}

int main()
{
    vector<int> v = {0, 4, 5, -1, 9, 9, 0, 54};
    func(v);
}
