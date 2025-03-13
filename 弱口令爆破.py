import jwt
import itertools

def generate_numeric_passwords(max_length=8):
    """生成1到max_length位的纯数字密码"""
    for length in range(1, max_length + 1):
        for password in itertools.product('0123456789', repeat=length):
            yield ''.join(password)

def detect_weak_jwt(token):
    """尝试使用1到8位纯数字密码破解JWT"""
    for password in generate_numeric_passwords():
        try:
            # 尝试使用当前密码解码JWT
            decoded = jwt.decode(token, password, algorithms=['HS256'])
            print(f"弱口令检测成功！使用的密码是: {password}")
            print(f"解码后的JWT内容: {decoded}")
            return password
        except jwt.InvalidTokenError:
            continue
        except jwt.DecodeError:
            continue
    print("未找到匹配的弱口令。")
    return None

if __name__ == "__main__":
    # 你的 JWT
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTc0MTg2NTM1NSwiZXhwIjoxNzQxODcyNTU1LCJuYmYiOjE3NDE4NjUzNTUsInN1YiI6InVzZXIiLCJqdGkiOiJmMWFmMmQwYWQ0NDkyOGE0OWVlOGZhZWMwMzg4NDkxZSJ9.fdZzh-Al_-y7vaykljjXj-U_BfBgw_lqsLyNWz5fqvk"

    # 检测弱口令
    detect_weak_jwt(token)