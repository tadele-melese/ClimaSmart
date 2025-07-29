import subprocess

def test_cli_help():
    result = subprocess.run(["python", "-m", "climasmart.cli", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "ClimaSmart" in result.stdout
