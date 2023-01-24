from dataclasses import dataclass

import toml


@dataclass
class Telegram:
    bot_token: str
    admin_id: int


@dataclass
class Database:
    dns: str


@dataclass
class Config:
    telegram: Telegram
    database: Database

    @classmethod
    def from_file(cls, path: str):
        raw_config = toml.load(path)
        return cls(
            telegram=Telegram(**raw_config["telegram"]),
            database=Database(**raw_config["database"]),
        )
