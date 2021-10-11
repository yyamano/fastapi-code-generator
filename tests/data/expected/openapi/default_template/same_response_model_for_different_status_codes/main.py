# generated by fastapi-codegen:
#   filename:  same_response_model_for_different_status_codes.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import Optional, Union

from fastapi import FastAPI, Path

from .models import Error, Pets

app = FastAPI(
    version='1.0.0',
    title='Swagger Petstore',
    license={'name': 'MIT'},
    description='This description is for testing\nmulti-line\ndescription\n',
)


@app.get('/pets', response_model=Pets, responses={'default': {'model': Error}})
def list_pets(limit: Optional[int] = None) -> Union[Pets, Error]:
    """
    List all pets
    """
    pass


@app.post('/pets', response_model=None, responses={'default': {'model': Error}})
def create_pets() -> Union[None, Error]:
    """
    Create a pet
    """
    pass


@app.get(
    '/pets/{pet_id}',
    response_model=Pets,
    responses={'404': {'model': Error}, 'default': {'model': Error}},
)
def show_pet_by_id(pet_id: str = Path(..., alias='petId')) -> Union[Pets, Error]:
    """
    Info for a specific pet
    """
    pass
