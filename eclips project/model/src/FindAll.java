import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class FindAll extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		//String n=request.getParameter("EName");
		//Integer e=Integer.parseInt(request.getParameter("ENo"));
		
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","1998");
	PreparedStatement st=con.prepareStatement("select * from addrecord ");
	//st.setInt(1, e);
	ResultSet rs=st.executeQuery();
	out.print("<body><a href=index.html><h3>Home page</h3></a>");
	out.println("<h1><center>satyam software solution </center></h1><hr>");
	out.print("<table>");
    out.print("<tr>");
     out.print("<th>EName</th>");
     out.print("<th>ENumber</th>");
     out.print("<th>ESalary</th>");
   out.print("</tr>");
   while(rs.next()){
  out.print("<tr>");
  out.print("<td>"+rs.getString(1)+"</td>");
  out.print("<td>"+rs.getInt(2)+"</td>");
  out.print("<td>"+rs.getInt(3)+"</td>");
  out.print("</tr>");

}
out.print("</table>");


}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }