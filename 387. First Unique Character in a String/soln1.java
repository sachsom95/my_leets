public class soln1 {

    HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
    int n = s.length();for(
    int i = 0;i<n;i++)
    {
        char c = s.charAt(i);
        dict.put(c, count.getOrDefault(c, 0) + 1);

    }

    for(
    int i = 0;i<n;i++)
    {
        if (count.get(s.charAt(i)) == 1)
            return i;
    }return-1;

}
