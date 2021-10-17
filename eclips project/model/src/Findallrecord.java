import java.io.*;
import java.sql.*;
import java.util.Iterator;
import java.util.List;
import java.util.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import model.*;

public class Findallrecord extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		//String n=request.getParameter("EName");
		//Integer e=Integer.parseInt(request.getParameter("ENo"));
		
        
try{  out.print("<body><a href=index.html><h3>Home page</h3></a>");
      out.println("<h1><center>satyam software solution </center></h1><hr>");
 
	   Record r=new Record();
	   List<Record>b=r.findallrecord();
	   Iterator<Record>it=b.iterator();
	 out.print("<table>");
     out.print("<tr>");
     out.print("<th>EName</th>");
     out.print("<th>ENumber</th>");
     out.print("<th>ESalary</th>");
     out.print("</tr>");
   while(it.hasNext()){
	   Record rs=(Record)it.next();
  out.print("<tr>");
    out.print("<td>"+rs.getEname()+"</td>");
    out.print("<td>"+rs.getEno()+"</td>");
    out.print("<td>"+rs.getEsalary()+"</td>");
  out.print("</tr>");

}
out.print("</table>");


}
catch (Exception e2) {System.out.println(e2);}
out.close();
} }