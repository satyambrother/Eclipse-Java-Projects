import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Login extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String u=request.getParameter("userid");
		String p=request.getParameter("password");
		//out.print(u);
		//out.print(p);
        
try{
	Class.forName("oracle.jdbc.driver.OracleDriver");
	Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	//out.print("connect");
	PreparedStatement ps=con.prepareStatement("select * from login where password=?");
	//ps.setString(1, u);
	ps.setString(1, p);
	ResultSet rs=ps.executeQuery();
	if(rs.next()){
		out.println("<h1><center>satyam software solution </center></h1><hr>");
	//out.print("<center><button href=Add.html> <a href=Add.html >addRecord </a></button></center>");
	//out.println(rs.getString(1)+"   "+rs.getInt(2));
	//out.print(u);
	//out.print(p);
	//while(rs.next()){
		
	if(u.equals(rs.getString(1)) && p.equals(rs.getString(2))){
	//if(u=="a" && p==1){
		
	
	out.print("<center><a href=record.html>click here</a> to go home page<center>");
	}}
	else{out.println("<h1><center>satyam software solution </center></h1><hr>");
		out.print("<h4>You entered wrong userid or password </h4>");
		out.print("<center><a href=login.html><h3> Click here goto the Login page</h3></a><center>");
		
	out.print("<center><h3><a href=register1.html>new user registration</a></3><center>");
	} }
catch (Exception e2) {System.out.println(e2);}
out.close();
}

}