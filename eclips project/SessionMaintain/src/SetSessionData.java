

import java.io.IOException;
import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class SetSessionData extends HttpServlet
{
	
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException
	{
		PrintWriter out=res.getWriter();
		
		req.getParameter("name");
		req.getParameter("email");
		HttpSession session=req.getSession();
		session.setAttribute("name",req.getParameter("name"));
		session.setAttribute("email",req.getParameter("email"));
		out.println("<h1>Session data is set<h1>");
		//session.setMaxInactiveInterval(10);
		
	}

	
}
