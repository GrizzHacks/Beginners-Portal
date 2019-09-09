
package pokedexentries;

public class PokedexEntries {

    public static void main(String[] args) {
//  TODO code application logic here
//  Used in the first portion of the tutorial:
//      System.out.println("Hello World!");
//  One way of declaring a new Pokemon object:
//      Pokemon Pikachu;
//      Pikachu = new Pokemon("Pikachu", 25, "Mouse Pokemon", 0.4, "Pichu, Raichu");

//  Creating our new Pokemon object
        Pokemon Pikachu = new Pokemon("Pikachu", 25, "Mouse Pokemon", 0.4, "Pichu, Raichu");
        
//  Seeing our Pikachu object before it is altered via methods
        System.out.println(Pikachu);
        
//  Testing the first two methods we created
        System.out.println(Pikachu.getNationalNumber());
        System.out.println(Pikachu.getPokemonName());
        
//  Altering the attributes of our Pokemon object
        Pikachu.changeDescription("Electric Mouse Pokemon");
        Pikachu.alterHeight(0.5);
        Pikachu.addEvolution("Alolan Raichu");
        
//  Seeing the results of our alteration
        System.out.println(Pikachu);
        
        
    }
    
}
