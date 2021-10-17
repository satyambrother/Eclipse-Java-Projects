package model;
import java.util.*;
import java.sql.*;
import javax.servlet.http.*;
import javax.servlet.ServletException;
public class Record extends HttpServlet {
	Connection  conn;
	PreparedStatement pst;
	ResultSet rs;
	private String sql;
	private Integer eno;
	private String ename;
	private Integer emo;
    private String email;
	
public void setEname(String ename)	
{
	this.ename=ename;
}

public void setEno(Integer eno)	
{
	this.eno=eno;
}
public void setEmo(Integer emo)	
{
	this.emo=emo;
}

public void setEmail(String email)	
{
	this.email=email;
}
public String getEname()
{
	return ename;
}
public Integer getEno() 
{
	return eno;
}
public Integer getEmo() 
{
	return emo;
}
public String getEmail()
{
	return email;
}
public Record() throws Exception
{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	
	conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
}
public void addrecord() throws Exception{

	sql="insert into addrecord11 values(?,?,?)";
	pst=conn.prepareStatement(sql);
	pst.setInt(1, eno);
	pst.setString(2, ename);
	pst.setInt(3, emo);
	pst.setString(4,email);
	
	pst.executeUpdate();
}}

