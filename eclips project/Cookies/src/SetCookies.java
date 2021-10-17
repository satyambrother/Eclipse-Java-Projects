

import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;


public class SetCookies extends HttpServlet
{ 
	protected void doGet(HttpServletRequest req,HttpServletResponse res) throws IOException,ServletException
	{
		Cookie cook=new Cookie("name",req.getParameter("name"));
		Cookie cook1=new Cookie("email",req.getParameter("email"));
		cook.setMaxAge(30);
		res.addCookie(cook);
		res.addCookie(cook1);
		PrintWriter out=res.getWriter();
		out.print("<h1>Cookies added in client browser <h1>");
	}
	

}
