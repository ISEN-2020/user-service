package com.usermanagement.controller;


import java.util.Arrays;
import java.util.List;
//java.lang.Object;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.usermanagement.model.User;
import com.usermanagement.model.Email;

import com.usermanagement.dao.UserDao;

@Controller
public class UserManagementController {
	
	@Autowired
	UserDao userDao;
	
	@RequestMapping(path = "/getUsers", method = RequestMethod.GET)
	public @ResponseBody List<User> getUsers() {
		return userDao.getUsers();
	}
	
	@RequestMapping(path = "/saveUser", method = RequestMethod.POST, produces=MediaType.APPLICATION_JSON_VALUE)
	public @ResponseBody User saveUser(@RequestBody User user) {
		System.out.println(user.getEmailAddress());
		return userDao.saveUser(user);
	}
	
	@RequestMapping(path = "/deleteUser", method = RequestMethod.POST, produces=MediaType.APPLICATION_JSON_VALUE)
	public @ResponseBody User deleteUser(@RequestBody int id) {
		User userToDelete = userDao.getUserById(id);
		userDao.deleteInBatch(Arrays.asList(userToDelete));
		return userToDelete;
	}

	@RequestMapping(path = "/deleteUserByEmail", method = RequestMethod.POST, produces=MediaType.APPLICATION_JSON_VALUE)
	public @ResponseBody User deleteUserByEmail(@RequestBody Email mail) {
		System.out.println(mail.getEmail());
		return userDao.deleteUserByEmail(mail.getEmail());
		
	}
}