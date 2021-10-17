import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Update extends HttpServlet {
	public void service(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		
		Integer e=Integer.parseInt(request.getParameter("ENo"));
		Float f=Float.parseFloat(request.getParameter("ESalary"));
		String s=request.getParameter("EName");
       
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	out.print("<a href=record.html><h3>Home page</h3></a>");
	PreparedStatement ps=con.prepareStatement("update addrecord set esalary=? where eno=?");
	
	ps.setFloat(1,f);
	ps.setInt(2,e);
	int i=ps.executeUpdate();
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	if(i>0)
	{ out.print("<h3>Your  employee  which name "+s+" update  successfully </h3>");
	  out.print("<h3><center>if you want to update more record <a href=Update.html>click here</a></center></h3>");
	  
	}
	
}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }