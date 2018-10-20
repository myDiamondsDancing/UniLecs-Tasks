public static int GetCountOfPoints(int N, int M, int A, int B)
{
    int count = N * (A - 1);
    if A % 2 = 1
    {
        count += B;
    }
    else
    {
        count += M - B + 1;
    }
    return count;

}

public static void Main()
{
    Console.WriteLine(string.format('Data : {0}, answer = {1}', GetCountOfPoints(10, 8, 4, 7));
    Console.WriteLine(string.format('Data : {0}, answer = {1}', GetCountOfPoints(10, 8, 7, 4));   
}
