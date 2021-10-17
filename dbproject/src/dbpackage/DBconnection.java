package dbpackage;
import java.sql.*;

public class DBconnection {
	
	public static void main(String[] args) 
    {   try
      {
        Class.forName("oracle.jdbc.OracleDriver");
        Connection con = DriverManager.getConnection("jdbc:oracle:oci8:@XE","system","satyam1998")) 
        Statement st=con.createStatement();
        ResultSet rs=st.executeQuery("SELECT * FROM EMP");
        while(rs.next())
        { System.out.println(rs.getInt(1)+".."+rs.getString(2)); }
         
        rs.close();
        st.close();
        con.close();
        }
        catch(Exception e){}
    }
}



