import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Add extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String n=request.getParameter("EName");
		Integer e=Integer.parseInt(request.getParameter("ENo"));
		Integer s=Integer.parseInt(request.getParameter("ESalary"));
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	out.print("connect");
	PreparedStatement ps=con.prepareStatement("insert into addrecord values(?,?,?)");
	ps.setString(1,n);
	ps.setInt(2,e);
	ps.setInt(3,s);
	
	int i=ps.executeUpdate();
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	if(i>0)
	out.print("You are successfully addrecord...");
	out.print("<center>if you want to add more record<a href=Add.html>click here</a></center>");
}
catch (Exception e2) {System.out.println(e2);}
out.close();
}

	private static void html(String string) {
		// TODO Auto-generated method stub
		
	} }