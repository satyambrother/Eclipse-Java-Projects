class Mix
{  public static void show()
    { System.out.println("hello"); }
 protected void display()
  {  System.out.println("satyam");}
                                 }
class Test extends Mix
{ public static void main(String args[])
  { show();
    Test d=new Test();
    d.display(); }
 }