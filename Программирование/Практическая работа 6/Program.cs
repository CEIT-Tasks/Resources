namespace Practice;
using static Console;
class Program
{
  static void Main(string[] args)
  {
    int n, sum = 0;
    Write("Enter the number n: ");
    n = int.Parse(ReadLine());
    int[,] arr = new int[n, n];

    var random = new Random();

    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        arr[i, j] = random.Next(-100, 100);
      }
    }

    for (int i = 0; i < n; i++)
    {
      WriteLine();
      for (int j = 0; j < n; j++)
      {
        Write("{0, 4}", arr[i,j]);
      }
    }
    WriteLine(); WriteLine();

    int m = 0;
    int[] plus = new int[n];

    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        if (arr[i, j] > 0)
        {
          m++;
        }
      }
      plus[i] = m;
      m = 0;
    }

    foreach (int elem in plus)
    {
      Write($"{elem} ");
    }

  }
}
