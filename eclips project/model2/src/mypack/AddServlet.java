package mypack;
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import dao.*;
import model.*;
public class AddServlet extends HttpServlet
{
	public void doPost(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException
	{
		res.setContentType("Text/html");
		PrintWriter out=res.getWriter();
		String userName=req.getParameter("userName");
		String userPassword=req.getParameter("userPassword");
		try
		{
			UserDao userDao=new UserDao();
			User user=new User();
			user.setUserName(userName);
			user.setUserPassword(userPassword);
			Integer x=userDao.addRecord(user);
			if(x>0)
			{
				out.println("Add record");
			}
			else
			{
				out.println("unknown error");
				
			}
		}
		catch(Exception e)
		{
			out.println(e);
		}
	}
}