package Project;

import java.util.ArrayList;
import java.util.Scanner;

public class Blackjack {
    public ArrayList<Cards> deck;
    public Player player1;
    public Player dealer;
    

    public Blackjack(Player player1, Player dealer){
        Cards cards = new Cards();
        //deck = cards.makeDeck();
        this.player1 = player1;
        this.dealer = dealer;
    }

    public static void score(Player player){
        boolean ace = false;
        for (Cards cards : player.hand) {
            if(cards.rank <= 10){
                player.score += cards.rank;
            }
            else if(cards.rank < 14){
                player.score += 10;
            }
            else{
                ace = true;
            }
            if(ace == true){
                if(player.score + 11 < 21){
                    player.score += 11;
                }
                else{
                    player.score += 1;
                }
            }
        }
    }

    public static void printPlayer(Player player){
        System.out.println(player.name);
        for (Cards cards : player.hand) {
            System.out.println(cards);
        }
        if(player.score <= 21){
            System.out.println("\n" + "Score: " + player.score);
        }
        else{
            System.out.println("\n" + "Score: " + player.score + "(busted)");
        }
    }

    public static void gameStatus(Player score, Player score2){
        if(score.score > 21 && score2.score > 21){
            System.out.println("This game ended in a draw!");
        }
        else if(score.score > 21  && score2.score < 21){
            System.out.println(score2.name + " has won the game!");
        }
        else if(score.score < 21  && score2.score > 21){
            System.out.println(score.name + " has won the game!");
        }
        else if(score.score == score2.score){
            System.out.println("This game ended in a draw!");
        }
        else if(score.score > score2.score){
            System.out.println(score.name + " has won the game!");
        }
        else if(score2.score > score.score){
            System.out.println(score2.name + " has won the game!");
        }
    }

    public static boolean dealerHS(Player p1, Player dealer){
        if (dealer.score < 17 || dealer.score < p1.score){
            return true;
        }
        else{
            return false;
        }
    }
    public static boolean playerHS(){
        boolean a = false;
        System.out.print("hit or stand: ");
        Scanner scan = new Scanner(System.in);
        char answer = scan.next().charAt(0);
        if(answer == 'H'|| answer == 'h'){a = true;}
        else if(answer == 's' || answer == 's'){a = false;}
        else{
            playerHS();
        }
        return a;
    }
    public static void main(String[] args) {
        Deck game = new Deck();
        Player player = new Player(game.deal(game.getDeck(), 2), "Brandon");
        Player dealer = new Player(game.deal(game.getDeck(), 2), "Dealer");
        score(player);
        score(dealer);
        // System.out.println(score1);
        // System.out.println(score2);
        System.out.println(player.hand);
        System.out.println(dealer.hand);
        if(playerHS() == true){
            System.out.println(player.name + " hits...");
            player.hand.add(deck.draw(deck.getDeck(), player.hand));
            printPlayer(player);
        }
        else{}
        if(dealerHS(player, dealer) == true){
            System.out.println("Dealer hits...");
            dealer.hand.add(deck.draw(deck.getDeck(), dealer.hand));
            printPlayer(dealer);
        }
        else{}
        // score1 = score(player);
        // score2 = score(dealer);
        gameStatus(player, dealer);
    }

}
