import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Register extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String n=request.getParameter("userName");
		String p=request.getParameter("password");
		
		
		try{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
		PreparedStatement ps=con.prepareStatement("insert into login values(?,?)");
		ps.setString(1,n);
		ps.setString(2,p);
		
		int i=ps.executeUpdate();
		out.println("<h1><center>satyam software solution </center></h1><hr>");
		if(i>0)
		out.print("<h4>You are successfully registered...</h4>");
		out.print("<center><a href=login.html><h3>go to the Login page</h3></a><center>");
		
		
			
		}catch (Exception e2) {System.out.println(e2);}
		
		out.close();
	}

}
