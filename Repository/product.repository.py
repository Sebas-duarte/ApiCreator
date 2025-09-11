from models.band_model import Band, Album
from sqlalchemy.orm import Session

class BandRepository:


    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_bands(self):

        return self.db.query(Band).all()

    def get_band_by_id(self, band_id: int):

        return self.db.query(Band).filter(Band.id == band_id).first()

    def create_band(self, name: str):

        new_band = Band(name=name)
        self.db.add(new_band)
        self.db.commit()
        self.db.refresh(new_band)
        return new_band

    def update_band(self, band_id: int, name: str = None):

        band = self.get_band_by_id(band_id)
        if band and name:
            band.name = name
            self.db.commit()
            self.db.refresh(band)
        return band

    def delete_band(self, band_id: int):

        band = self.get_band_by_id(band_id)
        if band:
            self.db.delete(band)
            self.db.commit()
        return band