import socket
import threading
import time

open_ports = []

target = input("Введите IP-адрес или домен: ")
start_port = int(input("Введите начальный порт: "))
end_port = int(input("Введите конечный порт: "))

def scan_port(port):
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(1)
        result = soc.connect_ex((target, port))
        if result == 0:
            print(f"[+] Порт {port} открыт")
            open_ports.append(port)
        soc.close()
    except Exception as ex:
        pass

start_time = time.time()

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print("\nСканирование завершено.")
print(f"Открытых портов найдено: {len(open_ports)}")
print(f"Время сканирования: {end_time - start_time:.2f} секунд")
