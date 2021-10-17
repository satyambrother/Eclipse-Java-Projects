package dao;
import java.sql.*;
import model.*;

public class UserDao
{ private Connection conn;
  private PreparedStatement pst;
  private ResultSet rs;
  private String sql;
  
  public UserDao() throws ClassNotFoundException,SQLException
  {
	  Class.forName("oracle.jdbc.driver.OraceDriver");
	  conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
  }

public Integer addRecord(User user) throws Exception{

	sql="insert into login1 values(?,?)";
	pst=conn.prepareStatement(sql);
	pst.setString(1, user.getUserName());
	pst.setString(2, user.getUserPassword());
	
	return pst.executeUpdate();
} }