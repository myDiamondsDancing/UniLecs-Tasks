using System;
using System.Linq;
					
public class Program
{
	public static int GetCountOfPoints(float[,] points)
	{
		int count = points.Lenght;
		
		for (int i = 0; i < points.Lenght - 1; i++)
		{
			float x1 = points[i, 0];
			float x2 = points[i + 1, 0];
			float y1 = points[i, 1];
			float y2 = points[i + 1, 1];
			
			float k = (y2 - y1) / (x2 - x1);
			float b = y2 - k * x2;
			
			for (float x = x1 + 1; x < x2; x++)
			{
				if ((k * x + b) % 1 == 0)
				{
					count += 1;
				}
			}
			
		}
		return count;
	}
	
	public static void Main()
	{
		Console.WriteLine("UniLecs");
		float[,] data = new float[,]
		{
			{1, 1}, {3, 3}, {4, 5}
		};	
		
		Console.WriteLine("Answer is {0}", GetCountOfPoints(data));
	}
}
