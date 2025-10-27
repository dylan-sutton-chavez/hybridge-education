# Facial Authenticator

> _Biometric authentication uses the physical characteristics of an individual—such as facial features, iris scans or fingerprints—to verify their identity before granting access to sensitive data or systems. Biometric identification is based on who the person is, rather than special knowledge or something the person has._ — (Matthew Kosinski and Jim Holdsworth, IBM)

## Requirements

- Python 3.9+
- deepface 0.0.95

`pip install -r requirements.txt`

## Usage

1. Initialize the object with the cache image

```python
face_authenticator = FaceAuthentication('img1.jpg') # initialize a face in cache (actor face)
```

2. Use the cache face and comparate with a given actor face

```python
result: bool = face_authenticator.verify_face('img2.jpg') # verify if the face is the same "actor face"

status: str = "is" if result else "isn't" # convert the result into an string (is, isn't)

print(f'The face {status} the same :)')
```

Output (the face is the same):

```bash
The face is the same :)
```

## Remember

- This module is a wrapper of the lbirary 'DeepFace' the usage depends of your computer software.
