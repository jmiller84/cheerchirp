from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.seed("seeds/cheerchirp.sql")


"""
When we visit the posts page
And submit the form to create a new post
We see the post on the page
"""
def test_create_post(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/cheerchirp.sql")
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name='title']", "My Day")
    page.fill("input[name='content']", "It was a good day")
    page.fill("input[name='user_id']", "1")
    page.click("text=Create Post")

    expect(page.locator(".t-title")).to_contain_text(["Test Title", "Test Post", "My Day"])
    expect(page.locator(".t-content")).to_contain_text(["Test Content", "Test Post Content", "It was a good day"])

# """
# When we create a new user using the signup page
# We 
# """

