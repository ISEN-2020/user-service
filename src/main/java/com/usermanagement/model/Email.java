package com.usermanagement.model;


import javax.persistence.*;
import java.util.Date;

public class Email {

	private String email;

	public Email() {

	}

	public Email(String email) {
		this.email=email;
	}
	


	public String getEmail() {
		return this.email;
	}
}