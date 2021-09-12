package Project;
public class Suit {
    public String suit;

    public Suit(String suit) throws IllegalArgumentException{
        if(suit.equals("Clubs")){
            this.suit = suit;
        }
        else if(suit.equals("Diamonds")){
            this.suit = suit;
        }
        else if(suit.equals("Hearts")){
            this.suit = suit;
        }
        else if(suit.equals("Spades")){
            this.suit = suit;
        }
        else{
            System.out.println("Please enter a correct suit: " + suit + " is not a correct suit.");
        }
    }
    public String getSuit() {
        return suit;
    }
    @Override
    public String toString() {
        return this.suit;
    }
}
