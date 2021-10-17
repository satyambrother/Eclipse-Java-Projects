import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Record extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String u=request.getParameter("username");
		Integer p=Integer.parseInt(request.getParameter("password"));
		String a="a";
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	out.print("connect");
	String s=request.getParameter("a");
	if(a.equals(s)){
		out.print("<a href=Add.html> Back </a>");
	}
	}
catch (Exception e2) {System.out.println(e2);}
out.close();
}

}