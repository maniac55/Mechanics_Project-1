package Project02.Preliminary;

import java.util.ArrayList;
import java.util.Scanner;

public class Parameters {

    static int g = 10;     //gravity 10 m/s^2
    static int m0 = 0;     //0 kg
    static double m1, m2, m3;
    static int t0;          //0 second
    static int t;
    static double f1, f2, f3;   //friction
    static double x1, y1, x2, y2, x3, y3;

    static Scanner scan = new Scanner(System.in);

    public static double frictionOne() {

        System.out.println("Input the friction for object 1:");
        Double inp = scan.nextDouble();
        if (inp < 0 || inp > 0.5) {
            System.out.println("Friction has to be between/including 0 and 0.5");
            return frictionOne();
        }
        f1 = inp;

        return f1;
    }

    public static double frictionTwo() {

        System.out.println("Input the friction for object 2:");
        Double inp = scan.nextDouble();
        if (inp < 0 || inp > 0.5) {
            System.out.println("Friction has to be between/including 0 and 0.5");
            return frictionTwo();
        }
        f2 = inp;

        return f2;
    }

    public static double frictionThree() {

        System.out.println("Input the friction for object 3:");
        Double inp = scan.nextDouble();
        if (inp < 0 || inp > 0.5) {
            System.out.println("Friction has to be between/including 0 and 0.5");
            return frictionThree();
        }
        f3 = inp;

        return f3;
    }

    public static double massOne() {
        System.out.println("Input the mass for object 1:");
        Double inp = scan.nextDouble();
        if (inp < 0 || inp > 10) {
            System.out.println("mass has to be between/including 0kg and 10kg");
            return massOne();
        }
        m1 = inp;

        return m1;
    }

    public static double massTwo() {
        System.out.println("Input the mass for object 2:");
        Double inp = scan.nextDouble();
        if (inp < 0 || inp > 10) {
            System.out.println("mass has to be between/including 0kg and 10kg");
            return massTwo();
        }
        m2 = inp;

        return m2;
    }

    public static double massThree() {
        System.out.println("Input the mass for object 3:");
        Double inp = scan.nextDouble();
        if (inp < 0 || inp > 10) {
            System.out.println("mass has to be between/including 0kg and 10kg");
            return massThree();
        }
        m3 = inp;

        return m3;
    }

    static ArrayList<Integer> times = new ArrayList<>();

    public static void time() {

        System.out.println("Do you want to input a new time?(if you want to add answer with yes otherwise is no)");
        String answer = scan.next();
        if (answer.equals("yes")) {
            System.out.print("please input your number: ");
            int inp = scan.nextInt();
            if (inp < 0) {          // a case if user mistakenly writes minus time
                System.out.println("The time cannot be minus. Try again.");
                time();
            }
            times.add(inp);
            time();
        }

    }

    public static void run() {       // to run the program
        massOne();
        massTwo();
        massThree();

        frictionOne();
        frictionTwo();
        frictionThree();

        time();
    }

    public static void main(String[] args) {

        run();

    }
}
