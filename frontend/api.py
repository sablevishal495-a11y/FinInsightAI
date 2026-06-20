import requests

# FastAPI Backend URL
BASE_URL = "http://127.0.0.1:8000"


def upload_pdf(uploaded_file):
    """
    Upload PDF to FastAPI backend
    """

    try:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        response = requests.post(
            f"{BASE_URL}/upload/",
            files=files,
            timeout=300
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }


def ask_question(question):
    """
    Ask question to backend
    """

    try:

        payload = {
            "question": question
        }

        response = requests.post(
            f"{BASE_URL}/query/",
            json=payload,
            timeout=300
        )

        if response.status_code == 200:
            return response.json()

        return {
            "answer": "Backend Error",
            "sources": []
        }

    except Exception as e:

        return {
            "answer": str(e),
            "sources": []
        }