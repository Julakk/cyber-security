# Container & Kubernetes Security Basics

Pengenalan kerentanan & best practice keamanan di lingkungan container (Docker) dan orchestration-nya (Kubernetes).

> ℹ️ Ini murni conceptual notes + checklist. Praktik hands-on butuh cluster Kubernetes (bisa pakai `minikube`/`kind` di lokal) yang di luar scope demo langsung di repo ini.

## 🐳 Docker Security

### Kerentanan Umum

1. **Running as root di dalam container** — kalau container ke-compromise, attacker langsung dapet privilege root di dalam container itu (dan berpotensi escape ke host kalau ada misconfig lain)
2. **Base image yang gak di-trust/outdated** — image dari sumber gak jelas atau versi lama yang punya CVE diketahui
3. **Secrets di-hardcode di Dockerfile/image layer** — `ENV API_KEY=xxx` di Dockerfile bakal ke-bake permanen di image history, bisa diekstrak siapa aja yang punya akses image
4. **Container privileged mode** (`--privileged`) — kasih akses hampir penuh ke host, harus dihindari kecuali benar-benar perlu
5. **Docker socket exposure** — mount `/var/run/docker.sock` ke dalam container = container itu bisa kontrol Docker daemon host (setara akses root host)

### Checklist Docker Security

- [ ] Container jalan sebagai **non-root user** (`USER` instruction di Dockerfile)
- [ ] Base image dari sumber terpercaya, scan pakai `docker scan` / `trivy` sebelum deploy
- [ ] Secrets pakai Docker secrets/environment injection saat runtime, **bukan** hardcoded di image
- [ ] Hindari `--privileged`, gunakan capability spesifik (`--cap-add`) kalau memang perlu
- [ ] Jangan mount Docker socket ke container kecuali benar-benar diperlukan (misal CI/CD runner tertentu)
- [ ] Set resource limits (`--memory`, `--cpus`) untuk mencegah resource exhaustion/DoS
- [ ] Image di-scan rutin untuk vulnerability (Trivy, Grype, atau built-in registry scanning)

### Contoh Dockerfile: Buruk vs Baik

```dockerfile
# ❌ BURUK
FROM ubuntu:18.04
ENV DB_PASSWORD=supersecret123
RUN apt-get update
COPY . .
CMD ["python3", "app.py"]
# Jalan sebagai root secara default, password ke-bake di image, base image outdated
```

```dockerfile
# ✅ BAIK
FROM python:3.12-slim
RUN useradd -m appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
USER appuser
# DB_PASSWORD diinject saat runtime (docker run -e / Kubernetes Secret), bukan di sini
CMD ["python3", "app.py"]
```

## ☸️ Kubernetes Security

### Kerentanan Umum

1. **RBAC terlalu longgar** — service account dengan permission `cluster-admin` padahal cuma butuh akses ke 1 namespace
2. **Pod Security tidak dikonfigurasi** — pod bisa jalan privileged, akses hostPath, atau hostNetwork tanpa restriction
3. **Secrets di ConfigMap** (bukan Secret object) — ConfigMap tidak di-encode/encrypt khusus, gampang kebaca
4. **Network Policy tidak ada** — default-nya semua pod bisa saling komunikasi bebas (flat network), memudahkan lateral movement kalau ada 1 pod ke-compromise
5. **Dashboard/API server exposed ke publik** tanpa autentikasi kuat

### Checklist Kubernetes Security

- [ ] **RBAC**: least privilege — service account cuma punya permission yang benar-benar dibutuhkan
- [ ] **Pod Security Standards**: enforce level `restricted` (non-root, no privilege escalation, dll) di namespace produksi
- [ ] **Secrets**: pakai `Secret` object (idealnya dengan encryption at rest aktif), jangan simpan credential di `ConfigMap`
- [ ] **Network Policies**: definisikan secara eksplisit siapa boleh komunikasi ke siapa (default deny, whitelist yang perlu)
- [ ] **API Server**: autentikasi kuat, gak exposed langsung ke internet tanpa proteksi tambahan
- [ ] **Image security**: sama seperti Docker — scan image, pakai `imagePullPolicy` yang tepat, sign image kalau memungkinkan
- [ ] **Audit logging** aktif untuk aksi-aksi sensitif di cluster

### Contoh: Pod Security Context

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
  containers:
    - name: app
      image: myapp:latest
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
```

Konfigurasi ini memastikan container: jalan sebagai user non-root, gak bisa privilege escalation, filesystem root read-only (mencegah modifikasi file di container saat runtime), dan drop semua Linux capabilities kecuali yang eksplisit ditambahkan.

## 📚 Sumber Belajar Lanjutan

- [OWASP Docker Top 10](https://owasp.org/www-project-docker-top-10/)
- [Kubernetes Security Documentation](https://kubernetes.io/docs/concepts/security/)
- Practice: TryHackMe room "Intro to container security" / "Kubernetes" learning path
- Tools buat dicoba: `trivy` (image scanning), `kube-bench` (CIS benchmark checker buat cluster)

## 🔗 Referensi

- Melengkapi [`cloud-security/s3-misconfig-checklist.md`](../s3-misconfig-checklist.md) — sama-sama soal kesalahan konfigurasi di infrastruktur modern, bukan cuma soal kerentanan kode
