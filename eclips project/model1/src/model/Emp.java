package model;
import java.sql.*;
import javax.servlet.http.*;
import javax.servlet.ServletException;
public class Emp extends HttpServlet{
	Connection  conn;
	PreparedStatement pst;
	private String sql;
	private String ename;
	private Integer eno;
    private Integer esalary;
	
public void setEname(String ename)	
{
	this.ename=ename;
}

public void setEno(Integer eno)	
{
	this.eno=eno;
}

public void setEsalary(Integer esalary)	
{
	this.esalary=esalary;
}
public String getEname()
{
	return ename;
}
public Integer getEno()
{
	return eno;
}
public Integer getEsalary()
{
	return esalary;
}
public Emp() throws Exception
{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
}
public void addrecord() throws Exception{
	sql="insert into addrecord values(?,?,?)";
	pst=conn.prepareStatement(sql);
	pst.setString(1, ename);
	pst.setInt(2, eno);
	pst.setInt(3, esalary);
	pst.executeUpdate();
}
}