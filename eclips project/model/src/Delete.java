import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

import model.*;

public class Delete extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		
		Integer e=Integer.parseInt(request.getParameter("eno"));
		
        
try{  out.println("<h1><center>satyam software solution </center></h1><hr>");
      Record m=new Record();
       m.setEno(e);
       m.deleterecord();	
	   out.print("<h1>You are delete record successfully<h1> ");
       out.print("<center>if you want to delete more record<a href=deleterecord.html>click here</a></center>");
}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }