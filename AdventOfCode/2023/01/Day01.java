import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day01 {

    private static void partOne() {
        List<String> data = new ArrayList<>();
        try {
            File file = new File("input.txt");
            try (Scanner scanner = new Scanner(file)) {
                while (scanner.hasNextLine()) {
                    data.add(scanner.nextLine());
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }
        int res = 0, num = 0;
        for (String line : data) {
            for (char ch : line.toCharArray()) {
                if (Character.isDigit(ch)) {
                    num = 10 * Character.getNumericValue(ch);
                    break;
                }
            }

            for (char ch : new StringBuilder(line).reverse().toString().toCharArray()) {
                if (Character.isDigit(ch)) {
                    num += Character.getNumericValue(ch);
                    break;
                }
            }
            res += num;
        }
        System.out.println(res);
    }

    private static void partTwo() {
        List<String> data = new ArrayList<>();
        try {
            File file = new File("input.txt");
            try (Scanner scanner = new Scanner(file)) {
                while (scanner.hasNextLine()) {
                    data.add(scanner.nextLine());
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }

        int d, res = 0, num = 0;
        for (String line : data) {
            for (int i = 0; i < line.length(); i++) {
                d = getDigit(line, i);
                if (d != -1) {
                    num = 10 * d;
                    break;
                }
            }

            for (int i = line.length() - 1; i >= 0; i--) {
                d = getDigit(line, i);
                if (d != -1) {
                    num += d;
                    break;
                }
            }
            res += num;
        }
        System.out.println(res);
    }

    private static Integer getDigit(String line, Integer idx) {
        char ch = line.charAt(idx);
        if (Character.isDigit(ch)) {
            return Character.getNumericValue(ch);
        }

        switch (ch) {
            case 'o':
                if (line.substring(idx, Math.min(line.length(), idx + 3)).equals("one")) {
                    return 1;
                }
                break;

            case 't':
                if (line.substring(idx, Math.min(line.length(), idx + 3)).equals("two")) {
                    return 2;
                } else if (line.substring(idx, Math.min(line.length(), idx + 5)).equals("three")) {
                    return 3;
                }
                break;

            case 'f':
                if (line.substring(idx, Math.min(line.length(), idx + 4)).equals("four")) {
                    return 4;
                } else if (line.substring(idx, Math.min(line.length(), idx + 4)).equals("five")) {
                    return 5;
                }
                break;

            case 's':
                if (line.substring(idx, Math.min(line.length(), idx + 3)).equals("six")) {
                    return 6;
                } else if (line.substring(idx, Math.min(line.length(), idx + 5)).equals("seven")) {
                    return 7;
                }
                break;

            case 'e':
                if (line.substring(idx, Math.min(line.length(), idx + 5)).equals("eight")) {
                    return 8;
                }
                break;

            case 'n':
                if (line.substring(idx, Math.min(line.length(), idx + 4)).equals("nine")) {
                    return 9;
                }
                break;

            default:
                break;
        }
        return -1;
    }

    public static void main(String[] args) {
        partOne();
        partTwo();
    }
}