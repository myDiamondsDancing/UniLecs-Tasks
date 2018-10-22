using System;

public class Programm
{
	public static int GetMaxElement(int[] arr)
	{
		int max = arr[0];
		foreach (int i in arr)
		{
			if (i > max)
			{
				max = i;
			}
		}
		return max;
	}
	
	public static int SumOfRange(int N)
	{
		int sum = 0;
		for (int i = 1; i < N + 1; i++)
		{
			sum += i;
		}
		return sum;
	}
	
	
	public static int GetMissedElement(int[] arr)
	{
		int max = GetMaxElement(arr);
		int fullSum = SumOfRange(max);
		int sum = 0;
		foreach (int num in arr)
		{
			sum += num;
		}
		return fullSum - sum;
	}
	
	public static void Main()
	{
		Console.WriteLine("Testing of GetMissedElement");
		int[] data = new int[] {1, 2, 3, 5};
		Console.WriteLine("Answer for {0} is {1}", data, GetMissedElement(data));
		
	}
}
