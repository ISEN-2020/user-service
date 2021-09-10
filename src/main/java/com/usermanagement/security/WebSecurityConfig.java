package com.usermanagement.security;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

	@Autowired
	DataSource dataSource;
	
	@Autowired
	public void configAuthentication(AuthenticationManagerBuilder auth) throws Exception {
		auth.jdbcAuthentication().dataSource(dataSource).passwordEncoder(NoOpPasswordEncoder.getInstance())
			.usersByUsernameQuery("SELECT email as username,password,enabled FROM user WHERE email=?")
			.authoritiesByUsernameQuery("SELECT email as username, role FROM user WHERE email=?");
	 }
	
	@Override
	protected void configure(HttpSecurity http) throws Exception {
	   http.authorizeRequests() 
				.antMatchers("/*").permitAll()
	   			.anyRequest().access("hasRole('ROLE_USER')")
	   	   .and()
	   	   		.formLogin()
	   	   			.loginPage("/login").permitAll()//.defaultSuccessUrl("/getUsers",true)
	   	   		
	   	   .and()
	   	   		.logout()
	   	   			.logoutRequestMatcher(new AntPathRequestMatcher("/logout"))
	   	   			.permitAll()
	   	   .and()
	   	   	.csrf().disable();
	 }
}
