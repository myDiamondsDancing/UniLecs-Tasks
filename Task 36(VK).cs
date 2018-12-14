using System;
					
public class Program
{
	public static int[] means_of_columns(int[,] matrix)
	{
		
		int rows = matrix.GetUpperBound(0) + 1;
		int columns = matrix.Length / rows;
		
		int[] means = new int[rows]; 
		
		for (int j = 0; j < columns; j++)
		{
			int sum = 0;

			for (int i = 0; i < rows; i++)
			{
				{
					sum += matrix[i, j]; 	
				}
			}
			
			means[j] = sum / rows;
		}		
		return means;	
	}	
	
	

	
	public static void Main()
	{
		int[,] test_data = new int[,] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 5, 7}};
		Console.Write(means_of_columns(test_data)[0]);
		Console.Write(" ");
		Console.Write(means_of_columns(test_data)[1]);
		Console.Write(" ");
		Console.Write(means_of_columns(test_data)[2]);		
	}
}
