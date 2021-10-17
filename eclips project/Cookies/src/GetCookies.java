
import java.io.*;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class GetCookies extends HttpServlet {
	
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException
	{
		Cookie ck[]=req.getCookies();
		PrintWriter out=res.getWriter();
		out.println(ck[0].getName()+"  "+ck[0].getValue().toString());
		out.println(ck[1].getName()+"  "+ck[1].getValue().toString());
		out.println(ck[0].getPath().toString()+" "+ck[0].getMaxAge());
		
	}

}
