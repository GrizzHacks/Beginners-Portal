
package pokedexentries;

public class Pokemon {
    
private String pokemonName;
private int nationalNumber;
private String shortDescription;
private double height;
private String evolutions;

//Sets up the Pokemon entry by taking in the Pokemon's name, National Number, a short description,
//its height, and its evolutions
public Pokemon(String name, int num, String description, double height, String evolutions)
{
    pokemonName = name;
    nationalNumber = num;
    shortDescription = description;
    this.height = height;
    this.evolutions = evolutions;
}
    
}
