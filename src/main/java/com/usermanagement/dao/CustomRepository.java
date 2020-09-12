package com.usermanagement.dao;

import java.util.List;

import com.usermanagement.model.User;

public interface CustomRepository {

	public List<User> getUsers();
	public User saveUser(User user);
	public User getUserById(int id);
	public void deleteUserById(int id);
	//public boolean login(String username, String password);
}
