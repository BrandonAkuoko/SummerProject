package Project;

import java.util.ArrayList;
import java.util.Random;

public class Deck {
    public ArrayList<Cards> deck;

    public Deck(){
        Cards d = new Cards();
        deck = d.makeDeck();
    }
    @Override
    public String toString() {
        for (Cards cards : deck) {
            return cards.toString();
        }
        return null;
    }
    public int deckSize(){
        return deck.size();
    }
    public ArrayList<Cards> getDeck() {
        return deck;
    }
    public void deal(ArrayList<Cards> deck, int number){
    
        // ArrayList<Cards> hand2 = new ArrayList<>();

        for (int i = 0; i < number; i++) {
            draw(deck);
            // draw(deck, hand2);
        }

    }
    public Cards draw(ArrayList<Cards> deck){
        Random random= new Random();
        if(deck.size() == 0){return null;}
        else{
            int temp = random.nextInt((deck.size() - 1) - 0);
            Cards drawn = deck.get(temp);
            // hand.add(drawn);
            return drawn;
        }
    }

    public static void main(String[] args) {
       Deck deck = new Deck();
       System.out.println(deck.deckSize()); //
    }
}
