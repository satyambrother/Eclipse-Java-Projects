

import java.io.*;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class GetHiddenData extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException
	{ 
		PrintWriter out=res.getWriter();
		out.println("Text Field name"+req.getParameter("name"));
		out.println("Hidden Field value"+req.getParameter("pass"));
		
		
	}

}
