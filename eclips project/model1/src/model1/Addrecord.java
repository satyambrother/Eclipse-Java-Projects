package model1;
import java.io.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import model.*;

public class Addrecord extends HttpServlet {
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType("text/html");
		PrintWriter out = response.getWriter();
		
		String n=request.getParameter("ename");
		Integer e=Integer.parseInt(request.getParameter("eno"));
		Integer s=Integer.parseInt(request.getParameter("esalary"));
        
try{
	Emp m=new Emp();
	m.setEname(n);
	m.setEno(e);
	m.setEsalary(s);
	m.addrecord();
	out.println("inserted");
	}
catch (Exception e2) {System.out.println(e2);}
out.close();
	} }