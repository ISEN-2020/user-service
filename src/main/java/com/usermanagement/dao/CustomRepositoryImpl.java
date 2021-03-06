package com.usermanagement.dao;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
import javax.persistence.PersistenceContext;
import javax.persistence.Query;
import javax.transaction.Transactional;

import org.springframework.stereotype.Repository;

import com.usermanagement.model.User;

@Repository
public class CustomRepositoryImpl implements CustomRepository {

	private static final String QUERY_GET_USER_BY_ID = "SELECT u.* FROM user.user AS u WHERE u.id = ?1" ;
	private static final String QUERY_GET_USERS = "SELECT u.* FROM user.user AS u";
	private static final String QUERY_SAVE_USER = "INSERT INTO user.user (name, email, password) VALUES ('%s','%s','%s')";
	private static final String QUERY_DELETE_USER_BY_EMAIL= "DELETE FROM user WHERE user.email = %s";
	private static final String QUERY_LOGIN = "SELECT COUNT(*) FROM user WHERE email=?1 AND password = ?2";

	@PersistenceContext
	EntityManager entityManager;
	
	@SuppressWarnings("unchecked")
	@Override
	public List<User> getUsers() {
		Query query = entityManager.createNativeQuery(QUERY_GET_USERS, User.class);
		return query.getResultList();
	}

	@Override
	@Transactional
	public User saveUser(User user) {
		Query query = entityManager.createNativeQuery(String.format(QUERY_SAVE_USER, user.getName(), user.getEmailAddress(), user.getPassword()), User.class);
		query.executeUpdate();
		return this.getUserById(user.getId());
	}

	@Override
	public User getUserById(int id) {
		Query query = entityManager.createNativeQuery(QUERY_GET_USER_BY_ID, User.class);
		query.setParameter(1, id);
		try{
		return (User) query.getSingleResult();
		}catch (NoResultException nre){
			//Ignore this because as per your logic this is ok!
			}
		return null;
	}
	@Override
	@Transactional
	public User deleteUserByEmail(String email) {
		System.out.println(email);
		Query query = entityManager.createNativeQuery(String.format(QUERY_DELETE_USER_BY_EMAIL, email, User.class));
		query.executeUpdate();
		return null;
	}
	
	
}
