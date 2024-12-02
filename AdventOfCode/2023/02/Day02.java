import java.util.List;
import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day02 {
    public static void main(String[] args) {
        Day02 day2 = new Day02();
        day2.partOne();
        day2.partTwo();
    }

    private void partOne() {
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

        int answer = 0;
        int red = 12, green = 13, blue = 14;

        outerloop:
        for (String line : data) {
            String[] splitLine = line.split(": ");
            int gameNumber = Integer.valueOf(splitLine[0].split(" ")[1]);

            for (String game : splitLine[1].split("; ")) {
                for (String cube : game.split(", ")) {
                    String[] splitCube = cube.split(" ");
                    int count = Integer.valueOf(splitCube[0]);
                    String color = splitCube[1];
                    switch (color) {
                        case "red":
                            if (count > red) {
                                continue outerloop;
                            }
                            break;

                        case "green":
                            if (count > green) {
                                continue outerloop;
                            }
                            break;

                        case "blue":
                            if (count > blue) {
                                continue outerloop;
                            }
                            break;

                        default:
                            break;
                    }
                }
            }
            answer += gameNumber;
        }
        System.out.println(answer);
    }

    private void partTwo() {
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

        int answer = 0;
        for (String line : data) {
            int red = 1, green = 1, blue = 1;
            for (String game : line.split(": ")[1].split("; ")) {
                for (String cube : game.split(", ")) {
                    String[] splitCube = cube.split(" ");
                    int count = Integer.valueOf(splitCube[0]);
                    String color = splitCube[1];
                    switch (color) {
                        case "red":
                            red = Math.max(red, count);
                            break;

                        case "green":
                            green = Math.max(green, count);
                            break;

                        case "blue":
                            blue = Math.max(blue, count);
                            break;

                        default:
                            break;
                    }
                }
            }
            answer += red * green * blue;
        }
        System.out.println(answer);
    }
}
