package com.usermanagement.controller;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class LoginController
{
	private final static String LOGINPATH="/login";
	
	/**
	 * The login page mapping method
	 * @return "login" string which is redirected into login.html using Thymeleaf.
	 */
	@RequestMapping(value=LOGINPATH, produces={MediaType.TEXT_HTML_VALUE}, method=RequestMethod.GET)
	public String loginPage()
	{
		return "login" ;
	}
}
