from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey, DateTime
from config import DATABASE_URL
from datetime import datetime, timezone

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Bases = declarative_base()

# Definindo os modelos
class Consultor(Bases):
    __tablename__ = 'Consultor'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    atuacao = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    avaliacoes = relationship("Avaliacao", back_populates="consultor")
    pedidos = relationship("Pedido", back_populates="consultor")

    def __repr__(self):
        return f"<Consultor(nome={self.nome}, email={self.email})>"

class Cliente(Bases):
    __tablename__ = 'Cliente'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    pedidos = relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(nome={self.nome}, email={self.email})>"

class Pedido(Bases):
    __tablename__ = 'Pedido'
    
    id = Column(Integer, primary_key=True, index=True)
    consultor_id = Column(Integer, ForeignKey('Consultor.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('Cliente.id'), nullable=False)
    status = Column(String, nullable=False)  # "pendente", "aceito", "recusado"
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Data de criação

    consultor = relationship("Consultor", back_populates="pedidos")
    cliente = relationship("Cliente", back_populates="pedidos")
    agenda = relationship("Agenda", back_populates="pedido", uselist=False)

    def __repr__(self):
        return f"<Pedido(consultor_id={self.consultor_id}, cliente_id={self.cliente_id}, status={self.status})>"

class Agenda(Bases):
    __tablename__ = 'Agenda'
    
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('Pedido.id'), nullable=False)
    assunto = Column(String, nullable=False)  # Nome do assunto da consultoria
    data = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Data de criação
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Data de atualização

    pedido = relationship("Pedido", back_populates="agenda")

    def __repr__(self):
        return f"<Agenda(assunto={self.assunto}, data={self.data}, horario={self.horario})>"

class Avaliacao(Bases):
    __tablename__ = 'Avaliacao'
    
    id = Column(Integer, primary_key=True, index=True)
    consultor_id = Column(Integer, ForeignKey('Consultor.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('Cliente.id'), nullable=False)
    nota = Column(Integer, nullable=False)  # Nota de 1 a 5
    comentario = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Data da avaliação

    consultor = relationship("Consultor", back_populates="avaliacoes")
    cliente = relationship("Cliente")  # Relacionamento apenas para referência

    def __repr__(self):
        return f"<Avaliacao(consultor_id={self.consultor_id}, nota={self.nota})>"

def init_db():
    Bases.metadata.create_all(engine)
