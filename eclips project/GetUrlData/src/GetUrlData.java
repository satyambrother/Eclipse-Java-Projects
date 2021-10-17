

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class GetUrlData extends HttpServlet
{
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException
	{
		String hdata,name;
		name=req.getParameter("name");
		hdata=req.getParameter("hiddendata");
		res.sendRedirect("RedirectedData?na="+name+"&hd="+hdata+"");
	}

}
