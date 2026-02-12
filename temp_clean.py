import httpx

BASE = "https://portfolio-reflex-pwdv.onrender.com"

# Login
print("Login...")
r = httpx.post(
    f"{BASE}/api/auth/login",
    data={"username": "admin", "password": "admin123"},
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    timeout=90.0,
)
print(f"Login: {r.status_code}")
if r.status_code != 200:
    print(r.text)
    exit(1)

token = r.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Ver visitas
r2 = httpx.get(f"{BASE}/api/analytics/recientes?limit=50", headers=headers, timeout=15.0)
if r2.status_code == 200:
    for v in r2.json():
        plat = v.get("plataforma", "")
        print(f"ID:{v['id']} | {v['timestamp'][:16]} | {v['pagina']} | {v['dispositivo']} | {v['navegador']} | {plat} | {v['ip']}")
else:
    print(f"Error: {r2.status_code} {r2.text}")
