class B extends A{
  int d,e,f;
  void mul(){
    f=d*e;
    System.out.println(f);
  }
  public static void main(String[] args){
    B obj=new B();
    obj.a=10;
    obj.b=20;
    obj.d=5;
    obj.e=10;
    obj.sum();
    obj.mul();
  }
}
class A{
  int a,b,c;
  void sum(){
  c=a+b;
  System.out.println(c);
}
}
