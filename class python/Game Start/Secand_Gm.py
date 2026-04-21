include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
void
shuffle (int arr[], int n)
{
  srand (time (0));
  for (int i = n - 1; i > 0; i--)
    {
      int j = rand () % (i + 1);
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
}

int
main ()
{
  char a[15], b[15], c[15], d[15], new[15];
  int e = 0, f = 0, g = 0, h = 0;
  printf ("Enter the four players name :");
  scanf ("%s%s%s%s", a, b, c, d);
  int nums[] = { 1000, 800, 500, 000 };
  int n = sizeof (nums) / sizeof (nums[0]);
  char choice;
  do
    {
      shuffle (nums, n);
      if (nums[0] == 1000 || nums[0] == 500)
	{
	  printf ("%s: %d\n", a, nums[0]);
	}
      if (nums[1] == 1000 || nums[1] == 500)
	{
	  printf ("%s: %d\n", b, nums[1]);
	}
      if (nums[2] == 1000 || nums[2] == 500)
	{
	  printf ("%s: %d\n", c, nums[2]);
	}
      if (nums[3] == 1000 || nums[3] == 500)
	{
	  printf ("%s: %d\n", d, nums[3]);

	}
      if (nums[0] == 500)
	{
	  printf ("%s tell us who is thief\n", a);
	  scanf ("%s", new);

	  if (strcmp (new, b) == 0)
	    {
	      if (nums[1] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[1] != 0)
		{
		  printf ("you are wrong\n");
		  nums[0] = 0;
		  if (nums[2] == 000)
		    nums[2] = 500;
		  else if (nums[3] == 000)
		    nums[3] = 500;
		}
	    }
	  else if (strcmp (new, c) == 0)
	    {
	      if (nums[2] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[2] != 000)
		{
		  printf ("you are wrong\n");
		  nums[0] = 0;
		  if (nums[1] == 000)
		    nums[1] = 500;
		  else if (nums[3] == 000)
		    nums[3] = 500;
		}
	    }
	  else if (strcmp (new, d) == 0)
	    {
	      if (nums[3] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[3] != 000)
		{
		  printf ("you are wrong\n");
		  nums[0] = 0;
		  if (nums[1] == 000)
		    nums[1] = 500;
		  else if (nums[2] == 000)
		    nums[2] = 500;
		}
	    }
	  else
	    {
	      printf ("you entered wrong name\n");
	    }
	}			// 0 ke liye work complete 
      else if (nums[1] == 500)
	{
	  printf ("%s tell us who is thief\n", b);
	  scanf ("%s", new);
	  if (strcmp (new, a) == 0)
	    {
	      if (nums[0] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[0] != 000)
		{
		  printf ("you are wrong\n");
		  nums[1] = 0;
		  if (nums[2] == 000)
		    nums[2] = 500;
		  else if (nums[3] == 000)
		    nums[3] = 500;
		}
	    }
	  else if (strcmp (new, c) == 0)
	    {
	      if (nums[2] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[2] != 000)
		{
		  printf ("you are wrong\n");
		  nums[1] = 0;
		  if (nums[0] == 000)
		    nums[0] = 500;
		  else if (nums[3] == 000)
		    nums[3] = 500;
		}
	    }
	  else if (strcmp (new, d) == 0)
	    {
	      if (nums[3] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[3] != 000)
		{
		  printf ("you are wrong\n");
		  nums[1] = 0;
		  if (nums[2] == 000)
		    nums[2] = 500;
		  else if (nums[0] == 000)
		    nums[0] = 500;
		}
	    }
	  else
	    {
	      printf ("you entered wrong name\n");
	    }
	}			// 1 index complete 
      else if (nums[2] == 500)
	{
	  printf ("%s tell us who is thief\n", c);
	  scanf ("%s", new);
	  if (strcmp (new, b) == 0)
	    {
	      if (nums[1] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[1] != 000)
		{
		  printf ("you are wrong\n");
		  nums[2] = 0;
		  if (nums[0] == 000)
		    nums[0] = 500;
		  else if (nums[3] == 000)
		    nums[3] = 500;
		}
	    }
	  else if (strcmp (new, a) == 0)
	    {
	      if (nums[0] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[0] != 000)
		{
		  printf ("you are wrong\n");
		  nums[2] = 0;
		  if (nums[1] == 000)
		    nums[1] = 500;
		  else if (nums[3] == 000)
		    nums[3] = 500;
		}
	    }
	  else if (strcmp (new, d) == 0)
	    {
	      if (nums[3] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[3] != 000)
		{
		  printf ("you are wrong\n");
		  nums[2] = 0;
		  if (nums[1] == 000)
		    nums[1] = 500;
		  else if (nums[0] == 000)
		    nums[0] = 500;
		}
	    }
	  else
	    {
	      printf ("you entered wrong name\n");
	    }
	}			// 2 index complete
      else if (nums[3] == 500)
	{
	  printf ("%s tell us who is thief\n", d);
	  scanf ("%s", new);
	  if (strcmp (new, b) == 0)
	    {
	      if (nums[1] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[1] != 000)
		{
		  printf ("you are wrong\n");
		  nums[3] = 0;
		  if (nums[0] == 000)
		    nums[0] = 500;
		  else if (nums[2] == 000)
		    nums[2] = 500;
		}
	    }
	  else if (strcmp (new, a) == 0)
	    {
	      if (nums[0] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[0] != 000)
		{
		  printf ("you are wrong\n");
		  nums[3] = 0;
		  if (nums[1] == 000)
		    nums[1] = 500;
		  else if (nums[2] == 000)
		    nums[2] = 500;
		}
	    }
	  else if (strcmp (new, c) == 0)
	    {
	      if (nums[2] == 000)
		{
		  printf ("you are right\n");
		}
	      else if (nums[2] != 000)
		{
		  printf ("you are wrong\n");
		  nums[2] = 0;
		  if (nums[1] == 000)
		    nums[1] = 500;
		  else if (nums[0] == 000)
		    nums[0] = 500;
		}
	    }
	  else
	    {
	      printf ("you entered wrong name\n");
	    }
	}
      printf ("%s: %d\t", a, nums[0]);
      printf ("%s: %d\t", b, nums[1]);
      printf ("%s: %d\t", c, nums[2]);
      printf ("%s: %d\n", d, nums[3]);
      e = e + nums[0];
      f = f + nums[1];
      g = g + nums[2];
      h = h + nums[3];
      if (e == f || e == g || e == h || f == g || f == h || g == h)
	{
	  printf ("you have to play 1-2 round because totals are equal\n");
	}
      printf ("Do you want to play again? (Y/N): ");
      scanf (" %c", &choice);
    }
  while (choice == 'Y' || choice == 'y');
  printf ("%s total = %d\n", a, e);
  printf ("%s total = %d\n", b, f);
  printf ("%s total = %d\n", c, g);
  printf ("%s total = %d\n", d, h);
  if (e > f && e > g && e > h)
    {
      printf ("FIRST RANK %s\n", a);
      if (f > g && f > h)
	{
	  printf ("SECOND RANK %s\n", b);
	  if (g > h)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", c, d);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", d, c);
	    }
	}
      else if (g > f && g > h)
	{
	  printf ("SECOND RANK  %s\n", c);
	  if (f > h)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", b, d);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", d, b);
	    }
	}
      else if (h > f && h > g)
	{
	  printf ("SECOND RANK %s\n", d);
	  if (g > f)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", c, b);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", b, c);
	    }
	}
    }				// e set completed
  else if (f > e && f > g && f > h)
    {
      printf ("FIRST RANK %s\n", b);
      if (e > g && e > h)
	{
	  printf ("SECOND RANK %s\n", a);
	  if (g > h)
	    {
	      printf ("THIRD RANK %s\nFOURTH RANK %s\n", c, d);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", d, c);
	    }
	}
      else if (g > e && g > h)
	{
	  printf ("SECOND RANK %s\n", c);
	  if (e > h)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", a, d);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", d, a);
	    }
	}
      else if (h > e && h > g)
	{
	  printf ("SECOND RANK %s\n", d);
	  if (g > e)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", c, a);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", a, c);
	    }
	}
    }				// f set is completed 
  else if (g > f && g > e && g > h)
    {
      printf ("FIRST RANK %s\n", c);
      if (f > e && f > h)
	{
	  printf ("SECOND RANK  %s\n", b);
	  if (e > h)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", a, d);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", d, a);
	    }
	}
      else if (e > f && e > h)
	{
	  printf ("SECOND RANK %s\n", a);
	  if (f > h)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", b, d);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", d, b);
	    }
	}
      else if (h > f && h > e)
	{
	  printf ("SECOND RANK  %s\n", d);
	  if (e > f)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", a, b);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", b, a);
	    }
	}
    }				//g index completed
  else if (h > f && h > g && h > e)
    {
      printf ("FIRST RANK  %s\n", d);
      if (e > f && e > g)
	{
	  printf ("SECOND RANK  %s\n", a);
	  if (g > f)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", c, b);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", b, c);
	    }
	}
      else if (f > e && f > g)
	{
	  printf ("SECOND RANK  %s\n", b);
	  if (e > g)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", a, c);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", c, a);
	    }
	}
      else if (g > f && g > e)
	{
	  printf ("SECOND RANK  %s\n", c);
	  if (e > f)
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", a, b);
	    }
	  else
	    {
	      printf ("THIRD RANK %s\n FOURTH RANK %s\n", b, a);
	    }
	}
    }
  else if (e == f || e == g || e == h || f == g || f == h || g == h)
    {
      printf ("the totals are equal of someone");
    }
  return 0;
}