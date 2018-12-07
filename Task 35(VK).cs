using System;
					
public class Program
{
	public static string GetMaxNumber(string first, string second)
	{
		// т.к. в начале строкого числа нет нулей,
		// то сначала сравниваем "числа" по длине
		if (first.Length > second.Length)
		{
			return first;
		}
		else if (first.Length < second.Length)
		{
			return second;
		}

		// если длина строковых чисел одинакова,
		// то последовательно сравниваем цифры старших разрядов "чисел"
		for (int i = 0; i < first.Length; i++)
		{
			int firstDigit =first[i];
			int secondDigit = Convert.ToInt32(second[i]);
			if (firstDigit > secondDigit)
			{
				return first;
			}
			else if (firstDigit < secondDigit)
			{
				return second;
			}
		}
		return first;
	}	
	
	public static void Main()
	{
		Console.WriteLine("UniLecs");
		string a = "987531234567891";
		string b = "1234";
		Console.WriteLine("Answer = {0}", GetMaxNumber(a, b)); 		
	}
}
