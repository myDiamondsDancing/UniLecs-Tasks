using System;
					
public class Program
{		
	public static void Main()
	{
		char[] arr1 = {'s', 's', 's', 's', 's', 'f', 'd'};
		char[] arr2 = {'%', '%', '%', '%', 'd', '%'};
		
		Console.WriteLine("Test 1 : " + hasFiveInRow('s', arr1));
		Console.WriteLine("Test 2 : " + hasFiveInRow('%', arr2));		
	}	
	
	public static bool hasFiveInRow(char e, char[] arr)
	{
		int k = 0;
		
		for (int i = 0; i < arr.Length; i++)
			{
				if (arr[i] == e)
				{
					k++;
				}
				else
				{
					k = 0;
				}	
			
				if (k == 5)
				{
					return true;
				}	
			}
		
		return false;
	}		
}
