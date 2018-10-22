using System;

public class Programm
{
	public static int getMaxSum(int[] arr)
	{
		int sum = 0;
		foreach (int i in arr)
		{
			if (i > 0)
			{
				sum += i;
			}
		}
		return sum;		
	}
	
	public static void Main()
	{
		Console.WriteLine("UniLecs");
		int[] data = new int[] {1, 2, -5, 7, -10, 2,};
		Console.WriteLine("Answer for {0} is {1}", data, getMaxSum(data));
	}
}
