import paramiko

# Define the SSH parameters
host = '169.254.1.1'
port = 22
username = 'admin'
passwords = ['bVmksnIlX4', '=;.9cTgm;:R\\T9x\\', 'x^UftfyJYbb`zk6h']

# Define the commands to reset the RF device
reset_commands = [
    'config reset',
    'reboot'
]

# Try each password until we successfully connect to the device
for password in passwords:
    try:
        # Create an SSH client and connect to the remote server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        # Execute the reset commands
        for cmd in reset_commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # Wait for the command to complete
            stdout.channel.recv_exit_status()

        # Close the SSH connection
        ssh.close()

        # If we successfully connected to the device, break out of the loop
        break

    except paramiko.AuthenticationException:
        # If the password is incorrect, print an error message and try the next password
        print(f"Failed to connect to {host} with password {password}")

else:
    # If we have tried all passwords and still couldn't connect to the device, print an error message
    print(f"Failed to connect to {host} with any of the provided passwords")
