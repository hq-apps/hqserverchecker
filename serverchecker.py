import requests
import socket

def check_web_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"{url} is up and running."
        else:
            return f"{url} returned status code: {response.status_code}."
    except requests.ConnectionError:
        return f"{url} is not reachable."

def ping_server(ip):
    try:
        socket.setdefaulttimeout(2)
        socket.gethostbyaddr(ip)
        return f"{ip} is reachable."
    except socket.herror:
        return f"{ip} is not reachable."

def main():
    url = input("Enter the web server URL (e.g., http://example.com): ")
    ip = input("Enter the server IP address (e.g., 192.168.1.1): ")

    web_server_status = check_web_server(url)
    print(web_server_status)

    server_ping_status = ping_server(ip)
    print(server_ping_status)

if __name__ == "__main__":
    main()
