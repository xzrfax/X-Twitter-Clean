from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import getpass

def setup_driver():
    # Chrome options for better performance
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')  # Start Chrome in incognito mode
    return webdriver.Chrome(options=options)

def wait_and_find_element(driver, by, value, timeout=10):
    """Wait for an element to appear and return it"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Element not found: {value}")
        return None

def delete_tweets(username, password):
    driver = setup_driver()
    try:
        # Login with the new X/Twitter URL
        driver.get("https://x.com/i/flow/login")
        
        # Fill in username
        username_field = wait_and_find_element(driver, By.NAME, "text")
        if username_field:
            username_field.send_keys(username)
            username_field.send_keys(Keys.RETURN)
        
        # Fill in password
        password_field = wait_and_find_element(driver, By.NAME, "password")
        if password_field:
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
        
        # Navigate to profile
        time.sleep(5)  # Wait for login to complete
        driver.get(f"https://x.com/{username}")
        
        tweets_deleted = 0
        reposts_removed = 0
        errors = 0
        last_height = 0
        
        # Start at the top
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        
        while errors < 10:
            try:
                # Try to find either a repost or tweet button
                repost_button = wait_and_find_element(driver, By.CSS_SELECTOR, 
                    'button[data-testid="unretweet"][aria-label*="Reposted"]', timeout=3)
                
                menu_button = wait_and_find_element(driver, By.CSS_SELECTOR, 
                    'button[data-testid="caret"]', timeout=3)
                
                if not repost_button and not menu_button:
                    # Only scroll if we don't find any buttons
                    driver.execute_script("window.scrollBy(0, 500);")
                    time.sleep(1)
                    
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        driver.refresh()
                        time.sleep(3)
                        driver.execute_script("window.scrollTo(0, 0);")
                        time.sleep(2)
                    last_height = new_height
                    continue
                
                # Process what we find (repost or tweet)
                if repost_button:
                    # Scroll to the repost button
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", repost_button)
                    time.sleep(1)
                    
                    try:
                        driver.execute_script("arguments[0].click();", repost_button)
                    except:
                        repost_button.click()
                    
                    time.sleep(1)
                    
                    # Click "Undo repost" in the menu
                    undo_button = wait_and_find_element(driver, By.XPATH,
                        '//span[text()="Undo repost"]')
                    if undo_button:
                        try:
                            undo_button.click()
                        except:
                            driver.execute_script("arguments[0].click();", undo_button)
                        
                        reposts_removed += 1
                        print(f"Repost removed! Total: {reposts_removed} reposts, {tweets_deleted} tweets")
                
                elif menu_button:
                    # Scroll to the menu button
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", menu_button)
                    time.sleep(1)
                    
                    try:
                        driver.execute_script("arguments[0].click();", menu_button)
                    except:
                        menu_button.click()
                    
                    time.sleep(1)
                    
                    # Click Delete
                    delete_button = wait_and_find_element(driver, By.XPATH, 
                        '//span[text()="Delete"]')
                    if delete_button:
                        delete_button.click()
                        
                        # Confirm deletion
                        confirm_button = wait_and_find_element(driver, By.XPATH, 
                            '//span[text()="Delete"]')
                        if confirm_button:
                            confirm_button.click()
                            tweets_deleted += 1
                            print(f"Tweet deleted! Total: {reposts_removed} reposts, {tweets_deleted} tweets")
                
                time.sleep(2)
                errors = 0
                
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                errors += 1
                time.sleep(2)
        
        print(f"\nScript completed. Removed: {reposts_removed} reposts, {tweets_deleted} tweets")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    print("X/Twitter Tweet Deleter")
    print("-" * 30)
    USERNAME = input("Enter your X/Twitter username: ")
    PASSWORD = getpass.getpass("Enter your X/Twitter password: ")
    
    print("\nScript starting... Press Ctrl+C to stop.")
    try:
        delete_tweets(USERNAME, PASSWORD)
    except KeyboardInterrupt:
        print("\nScript stopped by user.") 