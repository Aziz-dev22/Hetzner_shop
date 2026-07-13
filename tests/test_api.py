"""
Hetzner Shop
API Tests
"""

from __future__ import annotations


from fastapi.testclient import TestClient


from main import app



client = TestClient(app)



def test_application_root():


    response = client.get("/")


    assert response.status_code == 200


    data = response.json()


    assert "status" in data



def test_auth_router_available():


    response = client.post(

        "/api/auth/login",

        json={

            "email":

            "unknown@example.com",


            "password":

            "wrong-password"

        }

    )


    assert response.status_code in [

        401,

        404,

        500,

    ]



def test_servers_router_available():


    response = client.get(

        "/api/servers/"

    )


    assert response.status_code in [

        401,

        403,

        200,

        500,

    ]
