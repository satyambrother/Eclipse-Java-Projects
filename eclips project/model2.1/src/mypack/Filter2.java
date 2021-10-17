package mypack;
import javax.servlet.*;
import java.io.*;
public class Filter2 implements Filter
{ 
	
	
	public void init(FilterConfig sc){}
  
	public void doFilter(ServletRequest req,ServletResponse res,FilterChain fc) throws ServletException ,IOException
    {
	  res.setContentType("text/html");
	  PrintWriter out=res.getWriter();
	  
	  String userPassword=req.getParameter("userPassword");
	  if(userPassword.length()>6)
	  {
		  fc.doFilter(req,res);
      }
	  else
	  {
		  out.println("<h1>Check password length </h1>");
	  }
  }
  public void destroy(){}
}

