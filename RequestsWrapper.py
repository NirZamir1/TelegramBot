from requests import post,get,exceptions

def postMethod(path: str, body: {}):
    print("Post method")
    try: 
       res = post(path, body,timeout = 5)
       res.raise_for_status()
       return res
    except TimeoutError as e:
        print(f"Timeout Error: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def getMethod(path: str, body: {}):
    print("Get method")
    try: 
        res = get(path, body,timeout = 5)
        res.raise_for_status()
        return res
    except TimeoutError as e:
        print(f"Timeout Error: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None