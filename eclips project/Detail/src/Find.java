import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Find extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		//String n=request.getParameter("EName");
		Integer e=Integer.parseInt(request.getParameter("ENo"));
		
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	PreparedStatement st=con.prepareStatement("select * from addrecord where eno=?");
	st.setInt(1, e);
	ResultSet rs=st.executeQuery();
	out.print("<body><a href=record.html><h3>Home page</h3></a>");
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	
	out.print("ENMAE---ENO---ESALARY");
	rs.next();
	out.println("<br>");
	out.println(rs.getString(1)+"   "+rs.getInt(2)+"   "+rs.getInt(3));
	out.print("<center>if you want to find more record<a href=Find.html> click here</a></center>");	
}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }