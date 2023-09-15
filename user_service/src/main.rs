use rocket;
use serde::{Serialize, Deserialize};

mod models;
mod routes;

fn main() {
    rocket::ignite()
        .mount("/", routes![routes::users::all])
        .launch();
}