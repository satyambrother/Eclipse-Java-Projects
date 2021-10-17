
package Addrecord;
import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import model.*;
public class Addrecord extends HttpServlet 
{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		out.println("Hiii");
		Integer i=Integer.parseInt(request.getParameter("userid"));
		String n=request.getParameter("username");
		Integer mo=Integer.parseInt(request.getParameter("mobile"));
		String e=request.getParameter("email");
        
try
{
	Record m=new Record();
	m.setEno(i);
	m.setEname(n);
	m.setEmo(mo);
	m.setEmail(e);
	m.addrecord();
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	out.println("<h1>record inserted successfully</h1>");
	}
catch (Exception e2) 
	{
	System.out.println(e2);
	}
out.close();
	} }