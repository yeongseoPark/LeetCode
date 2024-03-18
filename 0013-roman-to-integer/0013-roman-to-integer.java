import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.AbstractMap;


class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = Stream.of(
                new AbstractMap.SimpleEntry<>('I', 1),
                new AbstractMap.SimpleEntry<>('V', 5),
                new AbstractMap.SimpleEntry<>('X', 10),
                new AbstractMap.SimpleEntry<>('L', 50),
                new AbstractMap.SimpleEntry<>('C', 100),
                new AbstractMap.SimpleEntry<>('D', 500),
                new AbstractMap.SimpleEntry<>('M', 1000)
        ).collect(Collectors.toMap(AbstractMap.SimpleEntry::getKey, AbstractMap.SimpleEntry::getValue));

        int ans = 0;
        char[] charArray = s.toCharArray();
        int i = 0;
        while (i < charArray.length) {
            if (charArray[i] == 'I' && i != charArray.length - 1) {
                if (charArray[i+1] == 'V') {
                    i += 2;
                    ans += 4;
                }
                else if (charArray[i+1] == 'X') {
                    i += 2;
                    ans += 9;
                } else {
                    ans += map.get(charArray[i]);
                    i += 1;
                }
            }
            else if (charArray[i] == 'X' && i != charArray.length - 1)
            {
                if (charArray[i+1] == 'L') {
                    i += 2;
                    ans += 40;
                }
                else if (charArray[i+1] == 'C') {
                    i += 2;
                    ans += 90;
                } else {
                    ans += map.get(charArray[i]);
                    i += 1;
                }
            }
            else if (charArray[i] == 'C' && i != charArray.length - 1) {
                if (charArray[i+1] == 'D') {
                    i += 2;
                    ans += 400;
                }
                else if (charArray[i+1] == 'M') {
                    i += 2;
                    ans += 900;
                } else {
                    ans += map.get(charArray[i]);
                    i += 1;
                }
            }
            else {
                ans += map.get(charArray[i]);
                i += 1;
            }
        }
        return ans;
    }
}