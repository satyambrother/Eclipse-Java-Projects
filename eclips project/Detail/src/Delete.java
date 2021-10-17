import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Delete extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		
		Integer e=Integer.parseInt(request.getParameter("ENo"));
		
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	//out.print("connect");
	PreparedStatement ps=con.prepareStatement("delete from addrecord  where eno=?");
	
	ps.setInt(1,e);
	
	
	int i=ps.executeUpdate();
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	if(i>0)
	{out.print("You are delete record successfully ");
	out.print("<center>if you want to delete more record<a href=Delete.html>click here</a></center>");
}}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }