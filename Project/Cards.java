package Project;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

import org.junit.Test.None;

/**
 * Creates the basic Cards for any sort of Card Game
 */
public class Cards {
    public int rank;
    public String suit;
    // public ArrayList<Cards> deck;

    public Cards(int rank, String suit){
        this.rank = rank;
        this.suit = suit;
    }
    public Cards(){
        super();
    }

    @Override
    /**
     * Sh
     */
    public String toString() {
        String shorthand = "" + rank + suit.charAt(0);
        if(rank <= 10){
            shorthand = "" + shorthand;
        }
        else if(rank == 11){
            shorthand = "J" + suit.charAt(0);
        }
        else if(rank == 12){
            shorthand = "Q" + suit.charAt(0);
        }
        else if(rank == 13){
            shorthand = "K" + suit.charAt(0);
        }
        else if(rank == 14){
            shorthand = "A" + suit.charAt(0);
        }
        
        if(suit.charAt(0) == 'H' || suit.charAt(0) == 'D'){
            shorthand = "\033[31m" + shorthand + "\033[37m";
        }
        else if(suit.charAt(0) == 'S' || suit.charAt(0) == 'C'){
            shorthand = "\033[34m" + shorthand + "\033[37m";
        }
        return shorthand;
    }
    /**
     * Used to create a deck of 52 cards, cards are addded to an ArrayList
     * As well as making the deck, it shuffles it also
     * @return deck
     */
    public ArrayList<Cards> makeDeck(){
        ArrayList<Cards> deck = new ArrayList<>();
        for (int i = 2; i < 15; i++) {
            deck.add(new Cards(i, "Hearts"));
        }
        for (int i = 2; i < 15; i++) {
            deck.add(new Cards(i, "Spades"));
        }
        for (int i = 2; i < 15; i++) {
            deck.add(new Cards(i, "Clubs"));
        }
        for (int i = 2; i < 15; i++) {
            deck.add(new Cards(i, "Diamonds"));
        }
        Collections.shuffle(deck);
        return deck;
    }
    /**
     * Might be extra but prints out the String of the whole deck
     * @param deck
     * @return cards.toString()
     */
    public String printDeck(ArrayList<Cards> deck){
        for (Cards cards : deck) {
            return cards.toString();
        }
        return suit;
    }
    /**
     * Function is used to draw a card from the deck and add it to the players "hand"
     * @param deck
     * @param hand
     * @return hand
     */
    // public ArrayList<Cards> draw(ArrayList<Cards> deck, ArrayList<Cards> hand){
    //     Random random= new Random();
    //     if(deck.size() == 0){return null;}
    //     else{
    //         int temp = random.nextInt((deck.size() - 1) - 0);
    //         Cards drawn = deck.get(temp);
    //         hand.add(drawn);
    //         return hand;
    //     }
    // }
    // /**
    //  * Deals cqrds to each hand one at a time.
    //  * @param deck
    //  * @param number
    //  * @return
    //  */
    // public ArrayList<Cards> deal(ArrayList<Cards> deck, int number){
    //     ArrayList<Cards> hand1 = new ArrayList<>();
    //     // ArrayList<Cards> hand2 = new ArrayList<>();

    //     for (int i = 0; i < number; i++) {
    //         draw(deck, hand1);
    //         // draw(deck, hand2);
    //     }
    //     return hand1;
    //}
    public int getRank() {
        return rank;
    }
    public String getSuit() {
        return suit;
    }

    public static void main(String[] args) {
        // int rank = 3;
        // String suit = "Diamonds";
        // Cards card = new Cards(rank, suit);
        ArrayList<Cards> deck = new Cards().makeDeck(); // use Blank Card constructor to make a deck
        for (Cards cards : deck) {
            System.out.print(cards + " "); // classic 52 deck: 2H 3H 4H 5H 6H 7H 8H 9H 10H JH QH KH AH 2S 3S 4S 5S 6S 7S 8S 9S 10S JS QS KS AS 2C 3C 4C 5C 6C 7C 8C 9C 10C JC QC KC AC 2D 3D 4D 5D 6D 7D 8D 9D 10D JD QD KD AD 
        }
    }
}
