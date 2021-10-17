package model;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class AddRecord extends HttpServlet 
{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		PrintWriter out = response.getWriter();
		String Name= request.getParameter("Name");
		String Department=request.getParameter("Department");
		String Eid =request.getParameter("Eid");
		String Mobile =request.getParameter("Mobile No");
		String Email=request.getParameter("Email Id");
		String Esal=request.getParameter("E-sal");
		
		try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
			out.print("connect");
			PreparedStatement ps=con.prepareStatement("insert into AddRecord1 values(?,?,?,?,?,?)");
			ps.setString(1,Name);
			ps.setString(2,Department);
			ps.setString(3,Eid);
			ps.setString(4,Mobile);
			ps.setString(3,Email);
			ps.setString(3,Esal);
			
			int i=ps.executeUpdate();
			if(i>0)
			out.print("You are successfully addrecord...");
			out.print("<a href=index.html> Back </a>");
			}
		catch (Exception e2)
		{
			System.out.println(e2);
		}
		out.close();
		}
	}


