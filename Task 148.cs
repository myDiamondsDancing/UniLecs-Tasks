using System;
					
public class Program
{
	
	public static int[] func(int[] arr)
	{
		int i = 0;
		
		for (int r = 0; r < arr.Length; r++)
		{
			if (arr[r] != 0)
			{
				arr2[i] = arr[r];
				i++;
			}	
		}
		
		int n = arr.Length - i;
		int j = i;
		
		for (int k = j; k < n; k++)
		{
			arr[k] = 0;
		}	
		
		return arr;
	}
	
	
	public static void Main()
	{
		int[] test = {0, 4, 5, -1, 9, 9, 0, 54};
		int[] answer = func(test);
		
		for (int i = 0; i < answer.Length; i++)
		{
			Console.Write(answer[i] + " ");
		}	
	}
}
