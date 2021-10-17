

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class NewServlet extends HttpServlet
{
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException
	{
	    String name,email;
	    HttpSession session=req.getSession();
	    name=(String)session.getAttribute("name");
	    email=(String)session.getAttribute("email");
	    PrintWriter out=res.getWriter();
	    out.println("name is "+name);
	    out.println("email is "+email);
	    out.print(session.getId());
	}

	
	

}
