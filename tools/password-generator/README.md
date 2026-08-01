# Password Generator

Generator password kuat/random pakai `secrets` module (cryptographically secure), plus estimasi kekuatan password (entropy).

## 🚀 Cara Pakai

```bash
python3 password_gen.py --length 16
python3 password_gen.py --length 20 --no-symbols
python3 password_gen.py --count 5   # generate 5 password sekaligus
```

## 🎓 Kenapa Pakai `secrets`, Bukan `random`?

Module `random` di Python pakai PRNG (pseudo-random) yang **predictable** kalau attacker tahu seed-nya — cocok buat simulasi/game, tapi TIDAK aman buat keperluan security seperti generate password/token. Module `secrets` pakai sumber randomness dari OS (cryptographically secure), yang didesain khusus buat keperluan seperti ini.
