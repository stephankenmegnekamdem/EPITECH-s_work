import java.util.ArrayList;
public class Ex05{
    public static ArrayList<String> myGetArgs(String... var){
        ArrayList<String> myArray = new ArrayList<String>();
        for(String s : var){
            myArray.add(s);
        }
        return myArray;
    }
}