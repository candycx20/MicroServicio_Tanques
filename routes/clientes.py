# routes/cliente_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal
from models.clientes import Cliente
from schemas.clientes import ClienteCreate

router = APIRouter()

@router.get("/clientes")
def get_clientes():
    db = SessionLocal()
    clientes = db.query(Cliente).all()
    db.close()
    return clientes

@router.get("/clientes/{cliente_id}")
def get_cliente(cliente_id: int):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    db.close()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/clientes/create")
def create_cliente(cliente: ClienteCreate):
    db = SessionLocal()
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente) 
    return db_cliente


