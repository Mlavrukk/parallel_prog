import numpy as np
import os
import time


def write_matrix(path: str, mt: np.array):
    with open(path, "w") as f:
        f.write(f"{np.shape(mt)[0]} {np.shape(mt)[1]}\n")
        for i in mt:
            for j in i:
                f.write(f"{j} ")
            f.write("\n")


def read_matrix(path: str) -> np.array:
    tmp = ""
    with open(path, "r") as f:
        tmp = f.readlines()
    tmp.remove(tmp[0])
    return np.array([[int(y) for y in x] for x in [x.strip().split(" ") for x in tmp]])


def verify_matmul(mt1: np.array, mt2: np.array, mt_res: np.array) -> bool:
    return np.array_equal(np.matmul(mt1, mt2), mt_res)


def genMatrix(a: int, b: int, c: int, path1: str, path2: str):
    row1 = a
    col1 = b
    row2 = col1
    col2 = c
    a = np.random.randint(0, 100, [row1, col1])
    b = np.random.randint(0, 100, [row2, col2])
    write_matrix(path1, a)
    write_matrix(path2, b)


if __name__ == "__main__":
    path_cpp = "C:/Users/every/source/repos/multithreading/Debug/multithreading.exe"
    path_res_template = "D:\git\multithreading\lab2/res/"
    thread_arr = [1,2, 4, 8, 12]
    
    a = 4
    b = 4
    c = 5
    for i_thread in thread_arr: 
        for i in range(5, 50, 5):
            for j in range(0, 10):
                genMatrix(a*i, b*i, c*i, "matrix1.txt", "matrix2.txt")    
                os.system(f"{path_cpp} {i_thread} {path_res_template}stats_lab2_t_{i_thread}")
                print(verify_matmul(read_matrix("matrix1.txt"), read_matrix(
                    "matrix2.txt"), read_matrix("res_cpp.txt")))
                
        print(f"finish thread = {i_thread}")
