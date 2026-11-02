public class Ex02 {
    public static String getAngryDog(int nbr){
        String bark = "";
        for(int i=1; i<=nbr; i++){
            bark = bark + "woof";
        }

        return bark + "\n";
    }
}