from concurrent.futures import process
from pymem import *

dll_path = input("DLL uzantısını girin: ")
dll_path_bytes = bytes(dll_path, "UTF-8")
process_name = input("Enjekte edilecek programın ismini girin: ")

open_process = Pymem(process_name)
process.inject_dll(open_process.process_handle, dll_path_bytes)

print("DLL başarıyla enjekte edildi")