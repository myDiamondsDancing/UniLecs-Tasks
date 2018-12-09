using System;
					
public class Program
{
	public static int[] find_in_matrix(int[,] matrix, int N)
	{
		int[] indexs = new int[] {-1, -1};
		
		int rows = matrix.GetUpperBound(0) + 1;
		int columns = matrix.Length / rows;
		
		for (int k = 1; k < columns; k++)
		{
			if (N < matrix[k, 0])
			{
				for (int j =0; j < rows; j++)
				{
					if (N == matrix[k - 1, j])
					{
						indexs[0] = k - 1;
						indexs[1] = j;
					}
				}	
			}	
		}
		
		for (int j = 0; j < rows; j++)
		{
			if (N == matrix[columns - 1, j])
			{
				indexs[0] = columns;
				indexs[1] = j;
			}
		}
			
		return indexs;	
	}	
	
	

	
	public static void Main()
	{
		int[,] test_data = new int[,] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
		int N = 8;
		Console.Write(find_in_matrix(test_data, N)[0]);
		Console.Write(" ");
		Console.Write(find_in_matrix(test_data, N)[1]);
	}
}
