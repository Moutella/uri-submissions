//Nome: Carrega ou não Carrega?
//Resultado: Compilation error
//Data: 06/05/16 15:07:46
//Linguagem: Java 7
import java.io.IOException;
import java.util.Scanner;

/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a, b;
        do {
            a = sc.nextLong();
            b = sc.nextLong();
            sc.nextLine();
            System.out.println(a ^ b);
        } while (sc.hasNextInt());
    }
 
}