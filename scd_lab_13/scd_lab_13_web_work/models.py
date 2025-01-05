# from sqlalchemy import Column, Integer, String
# from database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
# class User(Base):
#     __tablename__ = "users"

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    reset_token = Column(String, nullable=True)  # Add this column

    







# #     id = Column(Integer, primary_key=True, index=True)
# #     username = Column(String, unique=True, index=True)
# #     email = Column(String, unique=True, index=True)
# #     hashed_password = Column(String)
# #     reset_token = Column(String, nullable=True)
# #     token_expiry = Column(Integer, nullable=True)  # Expiry in seconds
# # from sqlalchemy import Column, Integer, String
# # from database import Base

# # class User(Base):
# #     __tablename__ = "users"
    
# #     id = Column(Integer, primary_key=True, index=True)
# #     username = Column(String, unique=True, index=True)
# #     email = Column(String, unique=True, index=True)
# #     hashed_password = Column(String)
# #     reset_token = Column(String, nullable=True)
# #     token_expiry = Column(Integer, nullable=True)  # Token expiry time in seconds (example: 3600 for 1 hour)
# # from sqlalchemy import Column, Integer, String
# # from database import Base

# # class User(Base):
# #     __tablename__ = "users"
    
# #     id = Column(Integer, primary_key=True, index=True)
# #     username = Column(String, unique=True, index=True)
# #     email = Column(String, unique=True, index=True)
# #     hashed_password = Column(String)
# #     reset_token = Column(String, nullable=True)
# #     token_expiry = Column(Integer, nullable=True)  # Token expiry time in seconds (example: 3600 for 1 hour)

# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime, timedelta
# import uuid

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     reset_token = Column(String, nullable=True)  # New column for reset token
#     reset_token_expires = Column(DateTime, nullable=True)  # Expiration time for token

#     def generate_reset_token(self):
#         """Generate a unique reset token."""
#         token = str(uuid.uuid4())
#         self.reset_token = token
#         self.reset_token_expires = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
#         return token














# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)

# class PasswordResetToken(Base):
#     __tablename__ = "password_reset_tokens"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     token = Column(String, unique=True, nullable=False)
#     user = relationship("User")
