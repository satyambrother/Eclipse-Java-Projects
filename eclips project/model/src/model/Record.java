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
public Record() throws Exception
{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	
	conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","1998");
}
public void addrecord() throws Exception{

	sql="insert into addrecord values(?,?,?)";
	pst=conn.prepareStatement(sql);
	pst.setString(1, ename);
	pst.setInt(2, eno);
	pst.setInt(3, esalary);
	
	pst.executeUpdate();
}

public void deleterecord() throws Exception{
	sql="delete from addrecord where eno=?";
	pst=conn.prepareStatement(sql);
	pst.setInt(1, eno);
	pst.executeUpdate();
}
public void updaterecord() throws Exception{
	sql="update addrecord set esalary=? where eno=?";
	pst=conn.prepareStatement(sql);
	//pst.setString(1, ename);
	
	pst.setInt(1, esalary);
	pst.setInt(2, eno);
	pst.executeUpdate();
}
public Record findrecord() throws Exception{

	sql="select * from addrecord where eno=?";
	pst=conn.prepareStatement(sql);
	pst.setInt(1, eno);
    rs=pst.executeQuery();
    if(rs.next())
    {  
    	Record n=new Record();
    	 n.setEname(rs.getString("ename"));
    	 n.setEno(rs.getInt("eno"));
    	 n.setEsalary(rs.getInt("esalary"));
    	return n;
    }
    else{
    	return null;
    }
}
public List<Record> findallrecord() throws Exception{

	sql="select * from addrecord ";
	pst=conn.prepareStatement(sql);
    rs=pst.executeQuery();
    List<Record> l=new ArrayList<Record>();
    while(rs.next())
    {  
    	 Record n=new Record();
    	 n.setEname(rs.getString("ename"));
    	 n.setEno(rs.getInt("eno"));
    	 n.setEsalary(rs.getInt("esalary"));
    	 l.add(n);
    }
	return l;
    
    
    
}
}