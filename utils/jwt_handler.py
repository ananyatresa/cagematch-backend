from fastapi import HTTPException, status
from firebase_admin import auth as firebase_auth


def verify_bearer_token(headers):
    """ Verifies Firebase ID token and returns decoded claims if valid. """
    try:
        auth_header = headers.get("authorization") or headers.get("Authorization")
        id_token = auth_header.split()[1]
        decoded_token = firebase_auth.verify_id_token(id_token, check_revoked=True)
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired/invalid. Please re-authenticate."
        )
