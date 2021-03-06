package assignment;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class FindAll extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private Connection conn;
	private PreparedStatement pst;
	private String sql;
	private ResultSet rs;
	private String name;
	private String department;
	private String eid;
	private Integer mobile;
	private String email;
	private Integer esal;
	private Integer sr;
	public Integer ctr=0;
	private FindAll f; 
	public FindAll() throws Exception
	{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		
		conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","satyam1998");
	
	}
	
       
   
	public void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{	
		
		response.setContentType(".jsp");
		PrintWriter out = response.getWriter();
		try
		{	
			setF(new FindAll());
			List<Object> l= findAllRecord();
			Iterator<Object> it=l.iterator();
			out.println("<table border='2'>");
			out.println("<tr><th> Name </th>");
			out.println("<th> Department </th>");
			out.println("<th> EID </th>");
			out.println("<th> Mobile </th>");
			out.println("<th> Email </th>");
			out.println("<th> ESAL </th>");
			out.println("<th> MODIFY </th>");
			out.println("<th> DELETE </th></tr>");
						
			while(it.hasNext())
			{	
				//ctr=ctr+1;
				FindAll fa = (FindAll)it.next();
				out.println("<tr id=ctr>");
				out.println("<td>");
				out.println(fa.getName());
				out.println("</td>");
				out.println("<td>");
				out.println(fa.getDepartment());
				out.println("</td>");
				out.println("<td>");
				out.println(fa.getEid());
				out.println("</td>");
				out.println("<td>");
				out.println(fa.getMobile());
				out.println("</td>");
				out.println("<td>");
				out.println(fa.getEmail());
				out.println("</td>");
				out.println("<td>");
				out.println(fa.getEsal());
				out.println("</td>");
				//out.println("<% int x=1 %>");
				out.println("<td>");
				out.println("<a href='modify?id="+ fa.getEid() +"'> MODIFY</a></td>");
				out.println(fa.getEid());
				out.println("<td>");
				out.println("<a href='' id=ctr> DELETE </a></td>");
				out.println("</tr>");
			
				//out.println(it.next());
			}
			out.println("</table>");
	
		}
		
		catch(Exception e)
		{
			out.println(e);
		}
		
	}
	public List<Object> findAllRecord() throws Exception
	{
		sql="select * from AddRecord1";
		pst=conn.prepareStatement(sql);
		rs=pst.executeQuery();
		List<Object> l = new ArrayList<Object>();
		while(rs.next())
		{
			FindAll fa = new FindAll();
			//fa.setSr(rs.getInt("sr"));
			fa.setName(rs.getString("Name"));
			fa.setDepartment(rs.getString("Department"));
			fa.setEid(rs.getString("EID"));
			fa.setMobile(rs.getInt("MOBILE"));
			fa.setEmail(rs.getString("EMAIL"));
			fa.setEsal(rs.getInt("esal"));
			l.add(fa);
			//System.out.println(l);
		}
		
		//System.out.println(l);
		return l;
	}



	public String getName() {
		return name;
	}



	public void setName(String name) {
		this.name = name;
	}



	public String getDepartment() {
		return department;
	}



	public void setDepartment(String department) {
		this.department = department;
	}



	public String getEid() {
		return eid;
	}



	public void setEid(String eid) {
		this.eid = eid;
	}



	public Integer getMobile() {
		return mobile;
	}



	public void setMobile(Integer mobile) {
		this.mobile = mobile;
	}



	public String getEmail() {
		return email;
	}



	public void setEmail(String email) {
		this.email = email;
	}



	public Integer getEsal() {
		return esal;
	}



	public void setEsal(Integer esal) {
		this.esal = esal;
	}



	public Integer getSr() {
		return sr;
	}



	public void setSr(Integer sr) {
		this.sr = sr;
	}



	public FindAll getF() {
		return f;
	}



	public void setF(FindAll f) {
		this.f = f;
	}



	
}
