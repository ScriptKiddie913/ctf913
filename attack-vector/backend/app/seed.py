from sqlalchemy.orm import Session
from app.core.db import SessionLocal, Base, engine
from app.core.security import get_password_hash
from app.core.config import settings
from app.models.user import User
from app.models.challenge import Category, Challenge
from app.utils.crypto import hash_flag

def seed():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        admin = db.query(User).filter_by(email=settings.ADMIN_EMAIL).first()
        if not admin:
            admin = User(email=settings.ADMIN_EMAIL, password_hash=get_password_hash(settings.ADMIN_PASSWORD), is_admin=True)
            db.add(admin)

        # Basic categories
        cat_names = [
            ("OSINT", "Storylined OSINT investigations with sequences."),
            ("Web", "Web exploitation challenges."),
            ("Crypto", "Cryptography challenges."),
            ("Forensics", "Forensic analysis challenges."),
        ]
        cats = {}
        for n, d in cat_names:
            c = db.query(Category).filter_by(name=n).first()
            if not c:
                c = Category(name=n, description=d)
                db.add(c)
            cats[n] = c
        db.commit()

        # Example OSINT storyline (sequence 1..n)
        osint = db.query(Category).filter_by(name="OSINT").first()
        if osint and not db.query(Challenge).filter_by(title="OSINT: The Vanishing Vendor 1").first():
            ch1 = Challenge(title="OSINT: The Vanishing Vendor 1",
                            description="Find the vendor's alias used on social media.",
                            difficulty="easy", points=100,
                            flag_hash=hash_flag("AV{alias_found}"), category_id=osint.id,
                            storyline="VanishingVendor", sequence=1)
            ch2 = Challenge(title="OSINT: The Vanishing Vendor 2",
                            description="Pivot to an email address from the alias.",
                            difficulty="medium", points=150,
                            flag_hash=hash_flag("AV{email_pivot}"), category_id=osint.id,
                            storyline="VanishingVendor", sequence=2)
            db.add_all([ch1, ch2])
            db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
