from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class GameOffsets:
    GOD_MODE: int = 0x2a4b3fc
    UNLIMITED_AMMO: int = 0x2a4b5ec
    ESP_ENABLED: int = 0x2a4b659
    SPEED_HACK: int = 0x2a4b61d
    NO_RECOIL: int = 0x2a4b7ef
    LOOT_UNLOCKER: int = 0x2a4b77f
    BOUNTY_COMPLETE: int = 0x2a4b874
    AIMBOT_FOV: int = 0x2a4b92e
    PLAYER_BASE: int = 0x1e8a470
    PLAYER_OFFSETS: list = field(default_factory=lambda: [0x0, 0x30, 0x8, 0x20])
    VERSION_OFFSETS: Dict[str, Dict[str,int]] = field(default_factory=lambda: {
        "2026.06.28-689": {
            "GOD_MODE": 0x2a4b3fc,
            "UNLIMITED_AMMO": 0x2a4b5ec,
        }
    })
    def get_for_version(self, ver): return self.VERSION_OFFSETS.get(ver, {})

offsets = GameOffsets()
