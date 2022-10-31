# 04_sys.path
import sys #내장모듈

print(sys.builtin_module_names) # Python 인터프리터 내장 모듈

for path in sys.path :
    print(path)