import paramiko

# Define the SSH parameters
host = '169.254.1.1'
port = 22
username = 'admin'
password = '=;.9cTgm;:R\\T9x\\'

# Define the commands to reset the RF device
reset_commands = [
    'config reset',
    'reboot'
]

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
