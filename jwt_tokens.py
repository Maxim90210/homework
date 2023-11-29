import datetime
import jwt
import settings

def generate_jwt_token(data, expiration_seconds=60):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_seconds)
    payload = {**data, "exp": expiration_time}

    encode_jwt = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )
    return encode_jwt


def decode_jwt_token(token):
    decoded = jwt.decode(
        token,
        settings.JWT_SECRET,
        algorithms=["HS256"],
    )
    return decoded

payload_data = {"my_name": "Maxim", "age": 13}
token = generate_jwt_token(payload_data)
print(token)

decoded_payload = decode_jwt_token(token)
print(decoded_payload)