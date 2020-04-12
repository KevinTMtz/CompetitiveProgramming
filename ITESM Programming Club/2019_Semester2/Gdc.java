class Gdc {
    public static void main(String[] args) {
        int a=366, b=60;
        System.out.println(gcd(a, b));
    }

    //Se usa el algoritmo de euclides para encontrar el MCD
    public static int gdc(int a, int b) {
        if (a != 0) {
            return gcd(b%a,a);
        } else {
            return b;
        }
    }
}