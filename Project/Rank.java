package Project;
public class Rank {
    public int rank;

    public Rank(int rank){
        this.rank = rank;
    }
    public int getRank() {
        return rank;
    }
    @Override
    public String toString() {
        return "" + rank;
    }
}
