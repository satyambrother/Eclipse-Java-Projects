import java.io.*;

import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import model.*;
public class Update extends HttpServlet {
	public void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		
		Integer e=Integer.parseInt(request.getParameter("eno"));
		Integer f=Integer.parseInt(request.getParameter("esalary"));
		String s=request.getParameter("ename");
       
try{
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	Record m=new Record();
	 m.setEname(s);
	 m.setEno(e);
	 m.setEsalary(f);
	 m.updaterecord();
    out.print("<h3>Your  employee  which name "+s+" update  successfully </h3>");
	out.print("<h3><center>if you want to update more record <a href=updaterecord.html>click here</a></center></h3>");
	  
	
	
}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }