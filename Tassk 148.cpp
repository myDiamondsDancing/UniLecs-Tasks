#include <iostream>
#include <vector>

using namespace std;

void func(vector<int> v)
{
	int i = 0;
		
	for (int r = 0; r < v.size(); r++)
	{
		if (v[r] != 0)
		{
			v[i] = v[r];
			i++;
		}	
	}
	
	for (int k = i; k < v.size(); k++)
	{
		v[k] = 0;
	}	
		
	for (int x = 0; x < v.size(); x++)
	{
	    cout << v[x] << endl;
	}
    
}

int main()
{
    vector<int> v = {0, 4, 5, -1, 9, 9, 0, 54};
    func(v);
}
