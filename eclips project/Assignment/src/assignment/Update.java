package assignment;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Update extends HttpServlet
{
	
	private static final long serialVersionUID = 1L;
	
	Connection conn;
	PreparedStatement ps;
    public Update() throws Exception 
    {
    	Class.forName("oracle.jdbc.driver.OracleDriver");
		 conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
    
    
    
    
    }

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{

		PrintWriter out = response.getWriter();
		String Name= request.getParameter("Name");
		String Department=request.getParameter("Department");
		String Eid =request.getParameter("Eid");
		String Mobile =request.getParameter("Mobile No");
		String Email=request.getParameter("Email Id");
		String Esal=request.getParameter("E-sal");
		try
		{
		 ps=conn.prepareStatement("update AddRecord1 set name=?,department=?,mobile=?,email=?,esal=? where eid = ?)");
		
		
		ps.setString(1,Name);
		ps.setString(2,Department);
		ps.setString(6,Eid);
		ps.setString(3,Mobile);
		ps.setString(4,Email);
		ps.setString(5,Esal);
		ps.executeUpdate();
		out.print("<h1>You are successfully updated record...</h1>");
		}
		catch(Exception e)
		{
			
		}
	}

}
