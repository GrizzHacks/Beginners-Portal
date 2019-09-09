
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


//Return the national number of a Pokemon.
public int getNationalNumber()
{
    return nationalNumber;
}

//Returns the name of a Pokemon
public String getPokemonName()
{
    return pokemonName;
}

//Changes the description of a Pokemon
public void changeDescription(String shortDescription)
{
    this.shortDescription = shortDescription;
}

//Changes the height of a Pokemon
public void alterHeight(double newHeight)
{
    height = newHeight;
}

//Adds evolutions to a Pokemon
public void addEvolution(String evolve)
{
    evolutions += ", " + evolve;
}

public String toString(){
    String result = "Pokemon Name: " + pokemonName + "\n";
    result += "National Number: " + nationalNumber + "\n";
    result += "Description: " + shortDescription + "\n";
    result += "Height (in meters): " + height + "\n";
    result += "Evolutions: " + evolutions;
    
    return result;
}

}
