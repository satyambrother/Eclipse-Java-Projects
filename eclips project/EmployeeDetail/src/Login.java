import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Login extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String u=request.getParameter("username");
		Integer p=Integer.parseInt(request.getParameter("password"));
		
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	out.print("connect");
	PreparedStatement ps=con.prepareStatement("select * from login where username=? and password=?");
	ps.setString(1, u);
	ps.setInt(2, p);
	ResultSet rs=ps.executeQuery();
	rs.next();
	out.println("login successful");
	out.print("<a href=record.html> main page </a>");
	}
catch (Exception e2) {System.out.println(e2);}
out.close();
}

}