def functionDirect():
    print("Yoda Direct")


def funcImported():
    print("Yoda Imported")


#! Normally, pyhton does automatically. But I can control myself. If "yoda.py" run byself, display the output "functionDirect", otherwise, "yoda.py" run inside another ".py" file, this time run "funcImported". "__name__" is handling that operation.
if __name__ == "__main__":
    functionDirect()
else:
    funcImported()
