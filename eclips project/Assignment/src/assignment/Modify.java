package assignment;

import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;



public class Modify extends HttpServlet {
	private static final long serialVersionUID = 1L;
    private Connection conn;
    PreparedStatement st;

    private String name;
	private String department;
	private String eid;
	private Integer mobile;
	private String email;
	private Integer esal;
	public String sr;
    public Modify() throws Exception
	{	
    	try
    	{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		
		conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
		
    	}
    	catch(Exception e)
    	{
    		
    	}
	}
    
	public void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{	
		try
		{
		Modify m = new Modify();
		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		/*out.println("<form action ='modify' method ='post'>");
out.println("Name       :  <input type='text' value=" + m.getName() + " name='Name'><br><br>");
out.println("Department : <input type ='text' value=" + department + " Name' name='Department'><br><br>");
out.println("Eid :        <input type='text' value=" + eid + " name='Eid'><br><br>");
out.println("Mobile No :  <input type='number value = " + mobile + " name='Mobile No'><br><br>");
out.println("Email Id :   <input type='email' value = " + email + " name='Email Id'><br><br>");
out.println("E-sal     : <input  type='number' value =" +esal + " name='E-sal'><br><br>");
out.println("<input type ='submit' value='SAVE '><br><br> </form> ");
	*/	
		
		sr =(request.getParameter("id"));
		
		PreparedStatement st=conn.prepareStatement("select * from AddRecord1 where eid=?");
		st.setString(1,sr);
		ResultSet rs=st.executeQuery();
		rs.next();
		
		m.setName(rs.getString("Name"));
		m.setDepartment(rs.getString("department"));
		m.setEid(rs.getString("eid"));
		m.setMobile(rs.getInt("mobile"));
		m.setEmail(email=rs.getString("email"));
		m.setEsal(esal=rs.getInt("esal"));
		
		
		out.println("<form action ='update' method ='post'>");
		out.println("Name       :  <input type='text' value=" + m.getName() + " name='Name'><br><br>");
		out.println("Department : <input type ='text' value=" + m.getDepartment() + " Name' name='Department'><br><br>");
		out.println("Eid :        <input type='text' value=" + m.getEid() + " name='Eid'><br><br>");
		out.println("Mobile No :  <input type='number value = " + m.getMobile()  + " name='Mobile No'><br><br>");
		out.println("Email Id :   <input type='email' value = " + m.getEmail() + " name='Email Id'><br><br>");
		out.println("E-sal     : <input  type='number' value =" + m.getEsal() + " name='E-sal'><br><br>");
		out.println("<input type ='submit' value='SAVE '><br><br> </form> ");
		out.println(sr);
		out.println(m.getMobile());
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		
		
		
	}
	
	
	
	
	
	
	

	public String getName() 
	{
		return name;
	}

	public void setName(String name) 
	{
		this.name = name;
	}

	public String getDepartment()
	{
		return department;
	}

	public void setDepartment(String department) 
	{
		this.department = department;
	}

	public String getEid() 
	{
		return eid;
	}

	public void setEid(String eid) 
	{
		this.eid = eid;
	}

	public Integer getMobile() 
	{
		return mobile;
	}

	public void setMobile(Integer mobile) 
	{
		this.mobile = mobile;
	}

	public String getEmail() 
	{
		return email;
	}

	public void setEmail(String email)
	{
		this.email = email;
	}

	public Integer getEsal() 
	{
		return esal;
	}

	public void setEsal(Integer esal)
	{
		this.esal = esal;
	}

}
