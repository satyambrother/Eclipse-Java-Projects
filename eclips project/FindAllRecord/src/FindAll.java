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
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	PreparedStatement st=con.prepareStatement("select * from addrecord ");
	//st.setInt(1, e);
	ResultSet rs=st.executeQuery();
	
	out.print("ENMAE---ENO---ESALARY");
	while(rs.next()){
	out.println("<br>");
	out.println(rs.getString(1)+"   "+rs.getInt(2)+"   "+rs.getInt(3));
	}
}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }