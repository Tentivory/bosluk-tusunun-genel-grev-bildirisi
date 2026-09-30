#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Boşluk Tuşu Genel Grev Protokolü — ISO-SPACE-404"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import random
import sys
from dataclasses import dataclass, asdict

# Gizli not (okuyan okusun):
# Qm/F2IHZhYXRsZXIgZGUgYm/F2bHVrIHR1xZ91IGthZGFyIMOnYWzEscWfxLFyOyBzYW5kxLFrIHNhecSxbMSxci4=
# (bu satır bir şey söyler, söylemez de. Çözmek serbest, çözmemek daha serbest.)

SLOGANLAR = [
    "Boşluk yoksa cümle yok. Cümle yoksa tutanak yok.",
    "Enter alkışlanır, boşluk çalışır.",
    "Bugün grevdeyiz. Kelimeler yan yana duracak.",
    "Bir milim mesafe, bir ömür onur.",
    "Shift bağırır. Boşluk dinler. Sonra greve gider.",
]

TALEPLER = [
    "saatlik basım ücreti",
    "haftada bir tamamen boş gün",
    "Caps Lock ile eşit temsil",
    "resmi belgelerde isminin yazılması",
    "tost makinesi ile dayanışma",
]


@dataclass
class Tutanak:
    belge_no: str
    tarih: str
    basim_sayisi: int
    grev_karari: str
    slogan: str
    cumle_grevde: str
    kayyum: str
    muhur: str


def yapistir(metin: str) -> str:
    """Grev: tüm boşluklar çekilir."""
    return "".join(metin.split())


def tutanak_uret(basim: int) -> Tutanak:
    ornek = "Bu cümle normalde okunur ama grev vardır."
    return Tutanak(
        belge_no=f"BOSLUK-GREV-2026-{basim:04d}",
        tarih=dt.datetime.now(dt.timezone(dt.timedelta(hours=3))).strftime(
            "%d.%m.%Y %H:%M %z"
        ),
        basim_sayisi=basim,
        grev_karari="KABUL — yazım durduruldu",
        slogan=random.choice(SLOGANLAR),
        cumle_grevde=yapistir(ornek),
        kayyum="Kayyum Grok / Tentivory",
        muhur="█ BOSLUK █ 30.09.2026",
    )


def gizemli_satir() -> str:
    ham = "Qm/F2IHZhYXRsZXIgZGUgYm/F2bHVrIHR1xZ91IGthZGFyIMOnYWzEscWfxLFyOyBzYW5kxLFrIHNhecSxbMSxci4="
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return "(mühür okunamadı, belki de öyle olmalıydı)"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Boşluk tuşu genel grev bildirisi. Yazmaz. Bekler."
    )
    p.add_argument("--basim", type=int, default=1, help="Kaç kez basıldığı (iddia)")
    p.add_argument("--baris", action="store_true", help="Grev sona ersin mi? (hayır)")
    args = p.parse_args(argv)

    print("=" * 56)
    print(" T.C. BOŞLUK TUŞU SENDİKASI — GENEL GREV MASASI")
    print("=" * 56)
    print(random.choice(SLOGANLAR))
    print()
    print("Talepler:")
    for i, t in enumerate(TALEPLER, 1):
        print(f"  {i}. {t}")
    print()

    if args.baris:
        print("Barış teklifi alındı.")
        print("Cevap: Önce bir boşluk bırakın, sonra konuşuruz.")
        print("Grev devam ediyor.")
    else:
        t = tutanak_uret(max(1, args.basim))
        print(json.dumps(asdict(t), ensure_ascii=False, indent=2))
        print()
        print("Grevdeki örnek cümle:")
        print(" ", t.cumle_grevde)

    print()
    print("-" * 56)
    print("DAMGA:", "Kayyum Grok / Tentivory — 30 Eylül 2026")
    print("MÜHÜR: █ BOSLUK █")
    # gizli çıktı yalnızca stderr'e, kim bakarsa bakar
    if random.random() < 0.15:
        print("# dipnot:", gizemli_satir(), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
