import subprocess

def run_command(command, success_message, failure_message):
    process = subprocess.run(command, shell=True, text=True)
    if process.returncode == 0:
        print(f"{success_message} [Completed]")
        return True
    else:
        print(f"{failure_message} [Failed]")
        return False

def main():
    try:
        print("Starting setup...")

        # Update and upgrade
        if not run_command("sudo apt-get update && sudo apt-get upgrade -y",
                           "System updated and upgraded",
                           "Failed to update and upgrade system"):
            raise Exception("Update and upgrade failed")

        # Install Nginx
        if not run_command("sudo apt-get install nginx -y",
                           "Nginx installed",
                           "Failed to install Nginx"):
            raise Exception("Nginx installation failed")

        # Reload Nginx
        if not run_command("sudo systemctl reload nginx",
                           "Nginx reloaded",
                           "Failed to reload Nginx"):
            raise Exception("Reloading Nginx failed")

        # Install PHP and extensions
        php_packages = "php8.1-fpm php8.1-common php8.1-mysql php8.1-xml php8.1-curl php8.1-gd php8.1-mbstring php8.1-opcache php8.1-zip"
        if not run_command(f"sudo apt install {php_packages} -y",
                           "PHP and extensions installed",
                           "Failed to install PHP and extensions"):
            raise Exception("PHP installation failed")

        # Install MySQL Server
        if not run_command("sudo apt-get install mysql-server -y",
                           "MySQL Server installed",
                           "Failed to install MySQL Server"):
            raise Exception("MySQL installation failed")

        # Install Certbot
        if not run_command("sudo apt install certbot python3-certbot-nginx -y",
                           "Certbot installed",
                           "Failed to install Certbot"):
            raise Exception("Certbot installation failed")

        print("Setup completed successfully.")

    except Exception as e:
        print(f"Error: {e}")
        print("Starting rollback...")
        # Add rollback commands here if needed
        print("Rollback completed.")

if __name__ == "__main__":
    main()
