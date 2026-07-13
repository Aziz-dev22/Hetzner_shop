"""
Hetzner Shop
Authentication Tests
"""

from __future__ import annotations


from fastapi.testclient import TestClient


from main import app



client = TestClient(app)



def test_root_available():


    response = client.get("/")


    assert response.status_code == 200



def test_register_endpoint_exists():


    response = client.post(

        "/api/auth/register",

        json={

            "email":

            "test@example.com",


            "username":

            "testuser",


            "password":

            "password123"

        }

    )


    assert response.status_code in [

        200,

        400,

        409,

        500,

    ]
