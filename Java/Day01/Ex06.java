public class Ex06 {
    public static void sequence(int nbr) {
        String var = "1";
        String temp = "";
        System.out.println(var);
        int count = 0;
        for (int i = 1; i <= nbr; i++) {
            temp = "";
            for (int j = 0; j < var.length();) {
                count = 0;
                char num = var.charAt(j);
                while (j < var.length() && var.charAt(j) == num  ) {
                    count++;
                    j++;
                }
                temp = temp + count + num;
            }
            var = temp;
            System.out.println(var);
        }
        System.out.println(var);
    }
}