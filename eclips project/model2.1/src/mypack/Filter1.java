package mypack;
import javax.servlet.*;
import java.io.*;
public class Filter1 implements Filter
{ 
	public void init(FilterConfig sc){}
    public void doFilter(ServletRequest req,ServletResponse res,FilterChain fc) throws ServletException ,IOException
  {
	  res.setContentType("text/html");
	  PrintWriter out=res.getWriter();
	  
	  out.println("FilterIN");
	  fc.doFilter(req,res);
	  out.println("Filter out");
  }
  public void destroy(){}
}

