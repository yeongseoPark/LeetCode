import java.math.BigInteger;


class Solution {
    public int[] plusOne(int[] digits) {
        StringBuilder s = new StringBuilder();

        for (int i = 0; i < digits.length; i++) {
            s.append(digits[i]);
        }

        BigInteger a = new BigInteger(s.toString());

        a = a.add(BigInteger.ONE);

        String string = a.toString();
        int[] ints = new int[string.length()];
        for (int i = 0; i < string.length(); i++)
        {
            ints[i] = Integer.valueOf(string.charAt(i) - '0');
        }

        return ints;
    }
}