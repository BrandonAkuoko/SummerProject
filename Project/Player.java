package Project;

import java.util.ArrayList;

public class Player {
    public ArrayList<Cards> hand;
    public String name;
    public int score;

    public Player(ArrayList<Cards> hand, String name){
        this.hand = hand;
        this.name = name;
        this.score = 0;
    }
    public String getName() {
        return name;
    }
    public void getHand() {
        for (Cards cards : hand) {
           System.out.print(cards);
        }
    }
    public int getScore() {
        return score;
    }

}
