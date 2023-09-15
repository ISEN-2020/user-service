use rocket_contrib::json::Json;
use crate::models::User;

#[get("/users")]
pub fn all() -> Json<Vec<User>> {
    // Fetch users from database or any other logic
    // Return as JSON
    Json(vec![
        User { id: 1, username: "user1".into(), email: "user1@mail.com".into() },
        User { id: 2, username: "user2".into(), email: "user2@mail.com".into() }
    ])
}


