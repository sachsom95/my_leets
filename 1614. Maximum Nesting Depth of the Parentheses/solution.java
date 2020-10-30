class Solution {
    public int maxDepth(String s) {
        int length = s.length();
        var depth = 0;
        var max = 0;
        for (int i = 0; i < length; i++) {
            if (s.charAt(i) == '(') {
                depth++;
                // if(max<depth) max = depth;
            } else if (s.charAt(i) == ')') {
                depth--;
            }
            if (max < depth)
                max = depth;
        }

        return max;

    }
}