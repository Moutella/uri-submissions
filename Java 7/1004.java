//Nome: Produto Simples
//Resultado: Accepted
//Data: 01/05/16 23:55:33
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
 
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("PROD = " + (a*b));
        
 
    }
 
}