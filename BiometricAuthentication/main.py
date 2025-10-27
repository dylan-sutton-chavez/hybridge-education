from deepface import DeepFace

class FaceAuthentication:
    def __init__(self, face_to_save: str):
        """
        initialize the `FaceAuthentication`

        args:
            face_to_save: str → receive the actor face path image

        output:
            None

        time complexity →o(1)
        """
        self.face_cache: str = face_to_save

    def verify_face(self, face: str):
        """
        whit a given face verify if the face is the same to the cache face

        args:
            face: str → receive the face to verify

        output:
            bool → True if its the same face, False if is not the same face

        time complexity → o(1)
        """
        result = DeepFace.verify(self.face_cache, face)
        return result['verified']
    
if __name__ == '__main__':
    """this block just run when the file is directly runed"""

    face_authenticator = FaceAuthentication('img1.jpg') # initialize a face in cache (actor face)
    result: bool = face_authenticator.verify_face('img2.jpg') # verify if the face is the same "actor face"

    status: str = "is" if result else "isn't" # convert the result into an string (is, isn't)

    print(f'The face {status} the same :)')