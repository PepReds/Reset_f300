import paramiko

def reset_device(ip_address):
    print(f"Resetting device at IP address: {ip_address}")
    try:
        # Create a new SSH client
        ssh_client = paramiko.SSHClient()
        # Automatically add the host key (don't use in production)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to the device
        ssh_client.connect(ip_address, username='admin', password='x^UftfyJYbb`zk6h')
        # Open a channel for sending CLI commands
        cli_channel = ssh_client.invoke_shell()
        # Send the necessary CLI commands to reset the device
        cli_channel.send('config reset\n')
        cli_channel.send('reboot\n')
        # Close the CLI channel
        cli_channel.close()
        # Close the SSH connection
        ssh_client.close()
        print("Device reset successfully")
    except Exception as e:
        print(f"Error resetting device: {e}")

# Example usage
ip_addresses = ['169.254.1.1']

for ip_address in ip_addresses:
    reset_device(ip_address)