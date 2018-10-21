using System;

public class Program
{

    public static int GetCountOfPoints(int N, int M, int A, int B)
    {
		int count = N * (A - 1);
		if (A % 2 == 1)
		{
			count += B;
		}
		else
		{
			count += N - B + 1;
		}
		return count;
    }

    public static void Main()
    {
        Console.WriteLine("GetCountOfPoints(10, 8, 4, 7) : {0}", GetCountOfPoints(10, 8, 4, 7));
        Console.WriteLine("GetCountOfPoints(10, 8, 7, 4) : {0}", GetCountOfPoints(10, 8, 7, 4));
		Console.WriteLine("GetCountOfPoints(3, 3, 2, 1) : {0}", GetCountOfPoints(3, 3, 2, 1)); 
    }
}
