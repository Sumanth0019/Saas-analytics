"""Helper: run schema + seed + train in correct order."""
import subprocess, sys

def run(cmd):
    print(f"\n▶ {cmd}")
    r = subprocess.run(cmd, shell=True)
    if r.returncode != 0:
        sys.exit(r.returncode)

if __name__ == "__main__":
    run("python backend/seed_data.py")
    run("python ml/train_model.py")
    print("\n✅ All set! Now run: streamlit run frontend/app.py")