import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import model.*;

public class Find extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		//String n=request.getParameter("EName");
		Integer e=Integer.parseInt(request.getParameter("eno"));
		
        
try{out.print("<body><a href=index.html><h3>Home page</h3></a>");
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	Record m=new Record();
	m.setEno(e);
	Record r=m.findrecord();
	out.print("ENMAE---ENO---ESALARY");

	out.println("<br>");
	out.println(r.getEname()+"   "+r.getEno()+"   "+r.getEsalary());
	out.print("<center>if you want to find more record<a href=findrecord.html> click here</a></center>");	
}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }